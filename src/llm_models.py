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

def similaritySearch(pergunta, k):
    return vectorstore.similarity_search_with_score(pergunta, k)

def invokePrompt(prompt, temperature):
  llm = ChatGoogleGenerativeAI(model=llm_model, temperature=temperature)
  resposta = llm.invoke(prompt)

  return resposta.content
