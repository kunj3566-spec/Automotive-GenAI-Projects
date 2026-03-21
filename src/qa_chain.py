from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from split_docs import split_documents


def build_vectorstore():
    chunks = split_documents()
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore


def ask_question(question: str):
    # 1. 建立向量库
    vectorstore = build_vectorstore()

    # 2. 先检索最相关内容
    docs = vectorstore.similarity_search(question, k=2)

    # 3. 拼接上下文
    context = "\n\n".join([doc.page_content for doc in docs])

    # 4. 调用 LLM
    llm = ChatOpenAI(model="gpt-4o-mini")

    prompt = f"""
You are an automotive AI assistant.

Answer the question concisely and clearly based on the context below.
Do not repeat the full context.
Summarize the key points.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content, docs


if __name__ == "__main__":
    question = "What is AUTOSAR?"
    answer, docs = ask_question(question)

    print(">>> ANSWER <<<")
    print(answer)

    print("\n>>> RETRIEVED DOCS <<<")
    for doc in docs:
        print("----")
        print(doc.page_content)