def main():
    try:
        saque = int(input("Digite o valor que deseja retirar:\n"))
        if saque <= 0 or saque % 2:
            raise ValueError
        else:
            contagemNotas(saque)
    except ValueError:
        print("Digite um valor positivo, inteiro e múltiplo de 2")

def contagemNotas(valor):
    nota100 = 0 
    nota50 = 0
    nota20 = 0 
    nota10 = 0 
    nota5 = 0 
    nota2 = 0
    sobra = 0
    while valor != 0:
        if valor - 100 >= 0:
            valor -= 100
            nota100 += 1
        
        elif valor - 50 >= 0:
            valor -= 50
            nota50 += 1
        
        elif valor - 20 >= 0:
            valor -= 20
            nota20 += 1
        
        elif valor - 10 >= 0:
            valor -= 10
            nota10 += 1
        
        elif valor - 5 >= 0:
            valor -= 5
            nota5 += 1

        elif valor - 2 >= 0:
            valor -= 2
            nota2 += 1
        else:
            sobra = valor
            valor -= 1
    print(f"""Foram utilizadas:\n
          {nota100} notas de R$100 reais.\n
          {nota50} notas de R$50 reais.\n
          {nota20} notas de R$20 reais.\n
          {nota10} notas de R$10 reais.\n
          {nota5} notas de R$5 reais.\n
          {nota2} notas de R$2 reais.\n
          Sobrou R$ {sobra} real.""")

if __name__ == "__main__":
    main()