import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
DATABASE_URL = os.getenv("DATABASE_URL")
COLLECTION_NAME = os.getenv("PG_VECTOR_COLLECTION_NAME")

def ingest_pdf():
    print("Lendo PDF")
    loader = PyPDFLoader(PDF_PATH)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = text_splitter.split_documents(docs)

    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)

    vectorstore = PGVector.from_documents(
        documents=chunks,
        embedding=embeddings,
        connection=DATABASE_URL,
        collection_name=COLLECTION_NAME
    )

    print("Ingestão concluída com sucesso!")



if __name__ == "__main__":
    ingest_pdf()