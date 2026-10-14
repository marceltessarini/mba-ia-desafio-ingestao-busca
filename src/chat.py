from search import search_prompt
from search_hyde import search_HyDE

def main():
    question = input("Faça sua pergunta: ")
    print("Pergunta: {0}\n\n".format(question))

    chain = search_HyDE(question)

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    
    print("\n\nResposta: {0}".format(chain))

if __name__ == "__main__":
    main()