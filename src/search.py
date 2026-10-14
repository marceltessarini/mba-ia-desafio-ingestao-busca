from prompts_mba import build_prompt_with_context
from llm_models import similarity_search, invoke_llm, format_chunks_as_string

def search_prompt(question):
  print("Search Direct RAG.")

  similarity_search_result = similarity_search(question, k=10)

  print("Gerando o prompt com contexto")
  context = format_chunks_as_string(similarity_search_result)
  prompt_with_context = build_prompt_with_context(context, question)

  print("Invocando LLM com contexto")

  response = invoke_llm(prompt_with_context, temperature=0)


  return response
