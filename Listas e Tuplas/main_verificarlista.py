def main ():
    lista = ["açucar", "sabao", "carne"]
    resposta = str
    while resposta != "sair":
        resposta = input("Digite o item que deseja verificar na lista (Digite 'sair' para sair): \n").lower()
        verificador(resposta, lista)

def verificador(resposta, lista):
    if resposta != "sair":
        if resposta in lista:
            print("Item encontrado, isso está na lista.")
        else:
            print(f"O item {resposta} que você procura não se encontra na lista. Precisa comprar!")
    else:
        print("Adie!")

if __name__ == "__main__":
    main()