from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from split_docs import split_documents
import os


def create_vector_store():
    # 1. 获取切分后的文档
    chunks = split_documents()

    # 2. 创建 embedding 模型
    embeddings = OpenAIEmbeddings()

    # 3. 构建向量数据库
    vectorstore = FAISS.from_documents(chunks, embeddings)

    return vectorstore


if __name__ == "__main__":
    print(">>> BUILDING VECTOR DB <<<")

    db = create_vector_store()

    # 测试检索
    query = "What is AUTOSAR?"
    results = db.similarity_search(query, k=2)

    print("\n>>> SEARCH RESULTS <<<")
    for r in results:
        print("----")
        print(r.page_content)