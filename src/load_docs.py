from langchain_community.document_loaders import TextLoader, PyPDFLoader
from pathlib import Path


def load_documents(data_dir="data/docs"):
    docs = []
    
    project_root = Path(__file__).resolve().parent.parent
    path = project_root / data_dir

    print(f"Looking for files in: {path}")

    for file in path.glob("*"):
        if file.suffix.lower() == ".txt":
            print(f"Loading TXT file: {file}")
            loader = TextLoader(str(file), encoding="utf-8")
            docs.extend(loader.load())

        elif file.suffix.lower() == ".pdf":
            print(f"Loading PDF file: {file}")
            loader = PyPDFLoader(str(file))
            docs.extend(loader.load())

    return docs


if __name__ == "__main__":
    documents = load_documents()
    print(f"Loaded {len(documents)} documents")

    for doc in documents:
        print("----")
        print(doc.page_content[:300])