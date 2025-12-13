import os

def main():
    print("Seja bem vindo ao clube de atletismo X.")
    listaPessoas = ['Ana', 'João', 'Carlos']
    resposta = str
    while True:
        print(f"Lista de nomes: {listaPessoas}")
        resposta = input("Digite o nome incorreto (ou 'sair' para encerrar): \n").lower()
        
        if resposta in listaPessoas:
            nomeCorrigir = listaPessoas.remove(resposta.capitalize())
            nomeCorrigir = input("Digite o nome corrigido: \n")
            listaPessoas.insert(999999, nomeCorrigir)
        elif resposta == 'sair':
            print("As pessoas cadastradas até o momento são: \n")
            for pessoa in listaPessoas:
                print(f"{pessoa}\t")
            break
        else:
            print("O nome dado não consta na lista, resetando programa...")
            os.system("pause")
            os.system('cls')
            main()

if __name__ == "__main__":
    main()