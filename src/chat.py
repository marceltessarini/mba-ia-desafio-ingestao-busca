import os
from dotenv import load_dotenv
from search import search_prompt
from search_hyde import search_HyDE

use_direct_rag_str = os.getenv("USE_DIRECT_RAG", "true")
use_direct_rag = use_direct_rag_str.strip().lower() == "true"

def main():
    question = input("Faça sua pergunta: ")
    print("Pergunta: {0}\n\n".format(question))

    if use_direct_rag: 
        chain = search_prompt(question)
    else:
        chain = search_HyDE(question)

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    
    print("\n\nResposta: {0}".format(chain))

if __name__ == "__main__":
    main()