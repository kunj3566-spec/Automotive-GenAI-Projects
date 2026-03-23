from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from embed_store import get_or_create_vectorstore


def ask_question(question: str, vectorstore):
    docs = vectorstore.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])

    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = f"""
You are an in-vehicle AI assistant for automotive systems.

Your job is to answer driver or passenger questions about vehicle functions, ADAS, AUTOSAR, OTA, diagnostics, and software architecture.

Rules:
- Answer clearly and concisely.
- Use only the context provided below.
- Do not repeat the full context.
- If the answer is not supported by the context, say you do not know.
- Keep the response safe and suitable for in-vehicle interaction.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content, docs


if __name__ == "__main__":
    print(">>> INITIALIZING VEHICLE KNOWLEDGE BASE <<<")
    vectorstore = get_or_create_vectorstore()

    while True:
        question = input("\nDriver asks (type 'exit' to quit): ")

        if question.lower() == "exit":
            print("Exiting assistant.")
            break

        answer, docs = ask_question(question, vectorstore)

        print("\n>>> VEHICLE ASSISTANT ANSWER <<<")
        print(answer)

        print("\n>>> RETRIEVED DOCS <<<")
        for doc in docs:
            print("----")
            print(doc.page_content)