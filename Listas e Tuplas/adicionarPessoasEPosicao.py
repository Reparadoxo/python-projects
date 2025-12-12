def main():
    print("Seja bem vindo ao evento X.")
    listaConvite = ['Ana', 'Pedro', 'Carlos']
    resposta = str
    while True:
        resposta = input("Digite o nome do novo convidado: (ou 'sair' para encerrar): \n").lower()
        print(f"A lista atual é: {listaConvite}\n")
        if resposta != 'sair':
            posicao = int(input("Digite a posição na qual deseja inserir o convidado:\n"))
            listaConvite.insert(posicao, resposta.capitalize())
        else:
            print("As pessoas cadastradas até o momento são: \n")
            for indice,pessoa in enumerate (listaConvite):
                print(f"Participante: {indice} --> Nome: {pessoa}\t")
            break

if __name__ == "__main__":
    main()