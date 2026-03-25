from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from src.embed_store import get_or_create_vectorstore


def main():
    # 只在启动时加载一次向量库
    db = get_or_create_vectorstore()
    retriever = db.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    print(">>> Automotive RAG Assistant Ready <<<")
    print("Type your question. Type 'exit' to quit.\n")

    while True:
        question = input("You: ").strip()

        if question.lower() in ["exit", "quit"]:
            print("Assistant: Bye!")
            break

        docs = retriever.invoke(question)
        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are an automotive in-vehicle AI assistant.
Answer the user's question only based on the context below.
If the answer is not in the context, say you do not know.

Context:
{context}

Question:
{question}
"""

        response = llm.invoke(prompt)

        print("\nAssistant:")
        print(response.content)
        print()


if __name__ == "__main__":
    main()