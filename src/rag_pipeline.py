from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from embed_store import get_vectorstore
from vehicle_tools import get_vehicle_speed, get_ota_status, get_dtc_codes



def retrieve_context(vectorstore, question, k=2):
    docs = vectorstore.similarity_search(question, k=k)
    context = "\n\n".join([doc.page_content for doc in docs])
    return context, docs


def format_chat_history(chat_history, max_turns=3):
    recent_history = chat_history[-max_turns:]
    history_text = ""

    for turn in recent_history:
        history_text += f"User: {turn['user']}\n"
        history_text += f"Assistant: {turn['assistant']}\n"

    return history_text


def generate_rag_answer(question, context, chat_history):
    llm = ChatOpenAI(model="gpt-4o-mini")

    history_text = format_chat_history(chat_history)

    prompt = f"""
You are an in-vehicle AI assistant for automotive systems.

Use the conversation history if it helps resolve references in the current question.
Answer the question concisely and clearly based on the context below.
Do not repeat the full context.
If the answer is not supported by the context, say you do not know.

Conversation history:
{history_text}

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content


def generate_tool_answer(question, tool_result, chat_history):
    llm = ChatOpenAI(model="gpt-4o-mini")

    history_text = format_chat_history(chat_history)

    prompt = f"""
You are an in-vehicle AI assistant.

Use the conversation history if it helps resolve the user's current request.

Conversation history:
{history_text}

A vehicle tool has returned the following data:
{tool_result}

User question:
{question}

Respond in a concise, driver-friendly way.
"""
    response = llm.invoke(prompt)
    return response.content


def handle_tool_call(question: str, chat_history):
    q = question.lower()

    if "speed" in q:
        result = get_vehicle_speed()
        return generate_tool_answer(question, result, chat_history), "get_vehicle_speed"

    if "ota status" in q or "update status" in q:
        result = get_ota_status()
        return generate_tool_answer(question, result, chat_history), "get_ota_status"

    if "dtc" in q or "trouble code" in q or "fault code" in q or "diagnostic code" in q:
        result = get_dtc_codes()
        return generate_tool_answer(question, result, chat_history), "get_dtc_codes"

    return None, None


def run_assistant(question, vectorstore, chat_history):
    tool_answer, tool_name = handle_tool_call(question, chat_history)

    if tool_answer:
        return {
            "mode": "tool",
            "tool_name": tool_name,
            "answer": tool_answer,
            "docs": []
        }

    context, docs = retrieve_context(vectorstore, question)
    answer = generate_rag_answer(question, context, chat_history)

    return {
        "mode": "rag",
        "tool_name": None,
        "answer": answer,
        "docs": docs
    }


if __name__ == "__main__":
    print(">>> INITIALIZING VECTOR DB <<<")
    vectorstore = get_vectorstore()
    chat_history = []

    while True:
        question = input("\nDriver asks (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        result = run_assistant(question, vectorstore, chat_history)

        print("\n>>> ASSISTANT ANSWER <<<")
        print(result["answer"])

        if result["mode"] == "tool":
            print(f"\n>>> TOOL USED <<<\n{result['tool_name']}")
        else:
            print("\n>>> RETRIEVED DOCS <<<")
            for doc in result["docs"]:
                print("----")
                print(doc.page_content)

        chat_history.append({
            "user": question,
            "assistant": result["answer"]
        })