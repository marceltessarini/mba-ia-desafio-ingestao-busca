from prompts_mba import buildDirectRAGPrompt
from llm_models import similaritySearch, invokePrompt

def search_prompt(pergunta=None):
  similaritySearchResult = similaritySearch(pergunta, k=10)

  contexto = "\n\n".join([doc.page_content for doc, score in similaritySearchResult])

  promptDirectRAG = buildDirectRAGPrompt(contexto=contexto, pergunta=pergunta)
  print("O prompt gerado eh {p}".format(p = promptDirectRAG))

  return invokePrompt(promptDirectRAG, temperature=0)


def main():
   resposta = search_prompt()
   print("Resposta: {0}".format(resposta))

if __name__ == "__main__":
    main()