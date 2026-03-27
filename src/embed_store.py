from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from split_docs import split_documents


INDEX_DIR = "faiss_index"


def build_and_save_vectorstore():
    chunks = split_documents()
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(INDEX_DIR)
    return vectorstore


def load_vectorstore():
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local(
        INDEX_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vectorstore


def get_vectorstore():
    index_path = Path(INDEX_DIR)

    if index_path.exists():
        print(">>> LOADING EXISTING FAISS INDEX <<<")
        return load_vectorstore()
    else:
        print(">>> BUILDING AND SAVING NEW FAISS INDEX <<<")
        return build_and_save_vectorstore()


if __name__ == "__main__":
    db = get_vectorstore()

    query = "What is AUTOSAR?"
    results = db.similarity_search(query, k=2)

    print("\n>>> SEARCH RESULTS <<<")
    for r in results:
        print("----")
        print(r.page_content)