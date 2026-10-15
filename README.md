# Ingestão e Busca Semântica com LangChain e Postgres

## Objetivo

O software capaz de realizar dois tipos de busca:

- Direct RAG
- HyDE

Os requisitos iniciais e obrigatório do projeto foram implementados na busca Direct RAG.
Podemos escolher o tipo de busca via variável de ambiente.

Para ambas as buscas, temos:

- Ingestão: Ler um arquivo PDF e salvar suas informações em um banco de dados PostgreSQL com extensão pgVector.
- Busca: Permitir que o usuário faça perguntas via linha de comando (CLI) e receba respostas baseadas apenas no conteúdo do PDF.

## Direct RAG x HyDE

* Direct RAG (`search.py`)

Na abordagem Direct RAG, a pergunta digitada pelo usuário é convertida diretamente em um vetor semântico e comparada contra os chunks armazenados no banco de dados.

* **Quando utilizar:**
  * **Dados específicos, privados ou tabulares:** Indicado para documentos que contêm dados altamente granulares, portfólios corporativos, tabelas de faturamento, nomes de empresas ou registros restritos que a LLM **não possui** em sua base de pré-treinamento.
  * **Exemplo prático:** Um PDF contendo uma tabela com o *Nome da Empresa*, *Faturamento* e *Ano de Fundação*. Como os dados são internos e desconhecidos do modelo, o Direct RAG garante que a busca ocorra estritamente sobre os fatos reais contidos na fonte, evitando alucinações.

* HyDE - Hypothetical Document Embeddings (`search_hyde.py`)

Na abordagem HyDE, a pergunta do usuário é primeiro enviada a uma LLM para que ela gere um **documento hipotético**. Esse documento hipotético é então vetorizado para realizar a busca semântica no banco de dados.

* **Quando utilizar:**
  * **Conteúdos conceituais, teóricos e públicos:** Indicado para documentos densos de domínio público ou geral, onde a LLM possui conhecimento prévio (como manuais teóricos, livros de metodologia, leis gerais ou guias de boas práticas).
  * **Exemplo prático:** Um PDF que funciona como um *manual de investimentos imobiliários* explicando conceitos como *Cap Rate*, estratégias de *Buy and Hold* ou análises de ativos. Perguntas vagas do usuário são traduzidas pela LLM em textos técnicos densos e ricos em vocabulário especializado, gerando um vetor de busca muito mais preciso para encontrar trechos teóricos correspondentes.

## Exemplo no CLI

Faça sua pergunta:

```
PERGUNTA: Qual o faturamento da Empresa SuperTechIABrazil?
RESPOSTA: O faturamento foi de 10 milhões de reais.

---

Perguntas fora do contexto:

PERGUNTA: Quantos clientes temos em 2024?
RESPOSTA: Não tenho informações necessárias para responder sua pergunta.
```

## Variáveis de ambiente

```
GOOGLE_API_KEY ou OPENAI_API_KEY dependendo do modelo escolhido.
EMBEDDING_MODEL
LLM_MODEL
DATABASE_URL
PG_VECTOR_COLLECTION_NAME
PDF_PATH
USE_DIRECT_RAG
```
- Se USE_DIRECT_RAG for true (padrão), então a busca Direct RAG será executada, caso contrário, HyDe será executada.


## Tecnologias obrigatórias

- Linguagem: Python
- Framework: LangChain
- Banco de dados: PostgreSQL + pgVector
- Execução do banco de dados: Docker & Docker Compose (docker-compose fornecido no repositório de exemplo)

## Pacotes recomendados

- Split: `from langchain_text_splitters import RecursiveCharacterTextSplitter`
- Embeddings (OpenAI): `from langchain_openai import OpenAIEmbeddings`
- Embeddings (Gemini): `from langchain_google_genai import GoogleGenerativeAIEmbeddings`
- PDF: `from langchain_community.document_loaders import PyPDFLoader`
- Ingestão: `from langchain_postgres import PGVector`
- Busca: `similarity_search_with_score(query, k=10)`


## VirtualEnv para Python

Crie e ative um ambiente virtual antes de instalar dependências:

```
python3 -m venv venv
source venv/bin/activate
```

## Ordem de execução

1. Subir o banco de dados:

```
docker compose up -d
```

2. Executar ingestão do PDF:

```
python src/ingest.py
```

3. Rodar o chat:

```
python src/chat.py
```


## Pré-requisitos

- **Python**: Versão `3.11.17` (recomendada)
- **Docker & Docker Compose**: Para execução do banco de dados PostgreSQL com pgVector

> **Nota sobre o ambiente Python:** Este projeto foi desenvolvido e testado utilizando o **Python 3.11.17**. Recomenda-se a utilização desta versão para garantir a compatibilidade com todas as dependências de IA (LangChain, PGVector, etc.). Fica a critério do avaliador utilizar o seu gestor de ambientes preferido (`venv`, `conda`, `pyenv`, etc.).