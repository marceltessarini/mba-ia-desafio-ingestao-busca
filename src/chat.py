import os
from dotenv import load_dotenv
from search import search_prompt
from search_hyde import search_HyDE

use_ryde_str = os.getenv("USE_RYDE", "false")
use_ryde = use_ryde_str.strip().lower() == "true"

def main():
    question = input("Faça sua pergunta: ")
    print("Pergunta: {0}\n\n".format(question))

    if use_ryde: 
        chain = search_HyDE(question)
    else:
        chain = search_prompt(question)

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    
    print("\n\nResposta: {0}".format(chain))

if __name__ == "__main__":
    main()