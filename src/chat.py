from search import search_prompt

def main():
    # TODO pedir para o usuario
    question = "Qual capital do Brasil?"
    chain = search_prompt(question)

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    
    print("Resultado: {0}".format(chain))

if __name__ == "__main__":
    main()