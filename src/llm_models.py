import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_postgres import PGVector
from langchain_core.prompts import PromptTemplate

load_dotenv()

connection = os.getenv("DATABASE_URL")
model_embeddings = os.getenv("GOOGLE_EMBEDDING_MODEL")
llm_model = os.getenv("GOOGLE_LLM_MODEL")
collections = os.getenv("PG_VECTOR_COLLECTION_NAME")

embeddings = GoogleGenerativeAIEmbeddings(model=model_embeddings)

vectorstore = PGVector(
    connection=connection,
    collection_name=collections,
    embeddings=embeddings
)

def similarity_search(pergunta, k):
    return vectorstore.similarity_search_with_score(pergunta, k)

def format_chunks_as_string(search_results):
    chunks_content = [doc.page_content for doc, score in search_results]

    return "\n\n".join(chunks_content)

def format_chunks_to_print(search_results):
    formated_chunks = []
    
    for i, (doc, score) in enumerate(search_results, start=1):
        block = f"--- Chunk {i} (Score: {score:.4f}) ---\n{doc.page_content}"
        formated_chunks.append(block)
        
    return "\n\n".join(formated_chunks)

def invoke_llm(prompt, temperature):
  llm = ChatGoogleGenerativeAI(model=llm_model, temperature=temperature)
  result = llm.invoke(prompt)

  return result.content
