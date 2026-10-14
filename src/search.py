from prompts_mba import build_direct_RAG_prompt
from llm_models import similarity_search, invoke_llm, format_chunks_as_string

def search_prompt(pergunta):
  print("Search.")

  similarity_search_result = similarity_search(pergunta, k=10)

  print("Gerando o prompt")
  context = format_chunks_as_string(similarity_search_result)
  prompt_direct_RAG = build_direct_RAG_prompt(contexto=context, pergunta=pergunta)

  print("Invocando LLM")

  result_llm = invoke_llm(prompt_direct_RAG, temperature=0)


  return result_llm
