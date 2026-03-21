from langchain_community.document_loaders import TextLoader
from pathlib import Path


def load_documents(data_dir="data/docs"):
    docs = []
    path = Path(data_dir)

    for file in path.glob("*.txt"):
        loader = TextLoader(str(file), encoding="utf-8")
        docs.extend(loader.load())

    return docs


if __name__ == "__main__":
    documents = load_documents()
    print(f"Loaded {len(documents)} documents")

    for doc in documents:
        print("----")
        print(doc.page_content[:200])