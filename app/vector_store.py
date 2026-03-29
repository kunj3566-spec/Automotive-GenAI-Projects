import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

RAW_DOCS_PATH = "data/raw_docs"
VECTOR_STORE_PATH = "data/vector_store"

def load_documents():
    documents = []

    for file_name in os.listdir(RAW_DOCS_PATH):
        file_path = os.path.join(RAW_DOCS_PATH, file_name)

        if file_name.endswith(".txt"):
            loader = TextLoader(file_path, encoding="utf-8")
            documents.extend(loader.load())

        elif file_name.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())

    return documents

def split_documents(documents):
    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)

def build_vector_store():
    documents = load_documents()
    chunks = split_documents(documents)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(chunks, embeddings)

    db.save_local(VECTOR_STORE_PATH)
    return db

def load_vector_store():
    embeddings = OpenAIEmbeddings()

    return FAISS.load_local(
        VECTOR_STORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

def get_or_create_vector_store():
    index_file = os.path.join(VECTOR_STORE_PATH, "index.faiss")

    if os.path.exists(index_file):
        print("Loading existing vector store...")
        return load_vector_store()
    else:
        print("Building new vector store...")
        return build_vector_store()