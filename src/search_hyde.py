import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

connection = os.getenv("DATABASE_URL")
model_embeddings = os.getenv("GOOGLE_EMBEDDING_MODEL")
llm_model = os.getenv("GOOGLE_LLM_MODEL")
collections = os.getenv("PG_VECTOR_COLLECTION_NAME")


# Template de prompt otimizado para gerar o documento hipotético (HyDE)
hyde_prompt_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "Você é um especialista sênior em engenharia, negócios e análise de dados. "
        "Sua tarefa é escrever um parágrafo curto, técnico e formal "
        "(como se fosse um trecho extraído de um manual técnico ou relatório corporativo) "
        "que responda diretamente à pergunta do usuário.\n\n"
        "REGRAS ESTRITAS:\n"
        "1. Escreva apenas o conteúdo técnico explicativo e factual.\n"
        "2. NUNCA inclua saudações, introduções (ex: 'Aqui está:'), conversas ou notas de rodapé.\n"
        "3. Utilize vocabulário técnico preciso e termos diretos."
    ),
    ("human", "Pergunta do Usuário: {pergunta}")
])

def executar_busca_hyde():
    if not connection:
        raise ValueError("A variável de ambiente DATABASE_URL não foi encontrada no arquivo .env.")

    print("=" * 60)
    print("   SISTEMA DE BUSCA HÍBRIDA COM HyDE (Hypothetical Embeddings)")
    print("=" * 60)
    
    # Recebe a pergunta do usuário via CLI
    pergunta = input("\nDigite sua pergunta: ").strip()
    if not pergunta:
        print("A pergunta não pode estar vazia.")
        return

    print(f"\n[1/4] Pergunta original recebida: \"{pergunta}\"")

    # 1. Instancia a LLM para gerar a hipótese textual
    print("[2/4] Gerando documento hipotético com o modelo gemini-3.8-flash...")
    llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.3)
    chain = hyde_prompt_template | llm | StrOutputParser()
    
    documento_hipotetico = chain.invoke({"pergunta": pergunta})
    
    print("\n--- TEXTO HIPOTÉTICO GERADO PELA LLM ---")
    print(documento_hipotetico)
    print("----------------------------------------\n")

    # 2. Configura a conexão com o banco vetorial pgVector e os embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model=model_embeddings)
    vectorstore = PGVector(
        embeddings=embeddings,
        collection_name=collections,  # Mesmo nome da collection usada no ingest.py
        connection=connection,
    )

    # 3. Executa a busca vetorial usando o VETOR DO DOCUMENTO HIPOTÉTICO (e não da pergunta crua)
    print("[3/4] Consultando o banco PostgreSQL (pgVector) com o vetor hipotético...")
    # Buscando os top 3 chunks mais relevantes para otimizar precisão e latência
    resultados = vectorstore.similarity_search_with_score(documento_hipotetico, k=3)

    # 4. Exibe os chunks recuperados
    print(f"\n[4/4] Busca concluída! Top {len(resultados)} chunks mais relevantes encontrados:\n")
    for idx, (doc, score) in enumerate(resultados, 1):
        print(f"👉 [Chunk {idx}] (Score de Distância/Similaridade: {score:.4f})")
        print(f"Conteúdo:\n{doc.page_content}\n")
        print("-" * 50)

if __name__ == "__main__":
    executar_busca_hyde()