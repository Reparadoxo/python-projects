import random

opcoes = ["pedra", "papel", "tesoura"]

print("Vamos jogar um jogo de Pedra, Papel e Tesoura. Escreva sua opção: \n")
escolhaH = str(input())

print("Certo, lá vai: \n")
escolhaC = random.choice(opcoes)

match escolhaH.lower():
    case "pedra":
        if escolhaC == "papel":
            print(f"Eu venci. Escolhi {escolhaC} conta o seu {escolhaH}.")
        elif escolhaC == "tesoura":
            print(f"Eu perdi. Escolhi {escolhaC} conta o seu {escolhaH}.")
        elif escolhaC == "pedra":
            print(f"Empatamos. Escolhi {escolhaC} conta o seu {escolhaH}.")
    case "papel":
        if escolhaC == "tesoura":
            print(f"Eu venci. Escolhi {escolhaC} conta o seu {escolhaH}.")
        elif escolhaC == "pedra":
            print(f"Eu perdi. Escolhi {escolhaC} conta o seu {escolhaH}.")
        elif escolhaC == "papel":
            print(f"Empatamos. Escolhi {escolhaC} conta o seu {escolhaH}.")
    case "tesoura":
        if escolhaC == "pedra":
            print(f"Eu venci. Escolhi {escolhaC} conta o seu {escolhaH}.")
        elif escolhaC == "papel":
            print(f"Eu perdi. Escolhi {escolhaC} conta o seu {escolhaH}.")
        elif escolhaC == "tesoura":
            print(f"Empatamos. Escolhi {escolhaC} conta o seu {escolhaH}.")
    case default:
        print("Sua escolha não existe.")