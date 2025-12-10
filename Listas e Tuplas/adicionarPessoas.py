def main():
    print("Seja bem vindo a ONG X.")
    listaPessoas = []
    resposta = str
    while resposta != 'sair':
        resposta = input("Digite o nome do voluntário (ou 'sair' para encerrar): \n").lower()
        if resposta != 'sair':
            listaPessoas.append(resposta.capitalize())
        else:
            print("As pessoas cadastradas até o momento são: \n")
            for pessoa in listaPessoas:
                print(f"{pessoa}\t")

if __name__ == "__main__":
    main()