from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from split_docs import split_documents


INDEX_DIR = "faiss_index"


def build_and_save_vectorstore(index_dir: str = INDEX_DIR):
    chunks = split_documents()
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(index_dir)
    return vectorstore


def load_vectorstore(index_dir: str = INDEX_DIR):
    index_path = Path(index_dir)
    if not index_path.exists():
        raise FileNotFoundError(f"Vector index not found: {index_dir}")

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load_local(
        index_dir,
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vectorstore


def get_or_create_vectorstore(index_dir: str = INDEX_DIR):
    index_path = Path(index_dir)

    if index_path.exists():
        print(">>> LOADING EXISTING VECTOR DB <<<")
        return load_vectorstore(index_dir)

    print(">>> BUILDING NEW VECTOR DB <<<")
    return build_and_save_vectorstore(index_dir)


if __name__ == "__main__":
    db = get_or_create_vectorstore()
    results = db.similarity_search("What is AUTOSAR?", k=2)

    print("\n>>> SEARCH RESULTS <<<")
    for r in results:
        print("----")
        print(r.page_content)