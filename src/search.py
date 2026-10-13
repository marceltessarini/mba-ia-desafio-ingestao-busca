import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_postgres import PGVector
from langchain_core.prompts import PromptTemplate
from prommpts_mba import TEMPLATE_PROMPT_DIRECT_RAG

load_dotenv()

# Conexão e Setup
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


def search_prompt(question=None):
  # 1. Passo: Receber a Pergunta
  pergunta = question

  # 2. Passo: Buscar k=10 no pgVector
  resultados = vectorstore.similarity_search_with_score(pergunta, k=10)

  # Concatenar os textos recuperados
  contexto = "\n\n".join([doc.page_content for doc, score in resultados])

  prompt = PromptTemplate.from_template(TEMPLATE_PROMPT_DIRECT_RAG)
  prompt_formatado = prompt.format(contexto=contexto, pergunta=pergunta)

  # 4. Passo: Chamar a LLM da Google
  llm = ChatGoogleGenerativeAI(model=llm_model, temperature=0)
  resposta = llm.invoke(prompt_formatado)

  return resposta.content


def main():
   resposta = search_prompt()
   print("Resposta: {0}".format(resposta))

if __name__ == "__main__":
    main()