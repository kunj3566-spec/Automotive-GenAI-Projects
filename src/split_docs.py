from langchain_text_splitters import RecursiveCharacterTextSplitter
from load_docs import load_documents


def split_documents():
    docs = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    split_docs = splitter.split_documents(docs)
    return split_docs


if __name__ == "__main__":
    print(">>> RUNNING SPLIT DOCS <<<")

    chunks = split_documents()
    print(f"Created {len(chunks)} chunks")

    for chunk in chunks:
        print("----")
        print(chunk.page_content)