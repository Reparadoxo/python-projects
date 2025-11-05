import random

def adivinhar_numero():
    numeroSecreto = int(random.randint(1, 100))
    
    while True:
        try:
            numeroEscolhido = int(input("Digite um palpite para o número secreto: \n"))
            if not 1 <= numeroEscolhido <= 100:
                    raise ValueError("Número fora do intervalo (1, 100).")

            if numeroSecreto == numeroEscolhido:
                print("Parabéns você acertou !")
                break
            elif numeroSecreto > numeroEscolhido:
                print("Errado, o número secreto é maior !")
            else:
                print("Errado, o número secreto é menor !")
        except ValueError as e:
            print(f"Entrada inválida: {e}") 


adivinhar_numero()