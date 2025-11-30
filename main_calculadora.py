try:
    num1 = float(input("Digite o primeiro número da calculadora:\n"))
    sinais = input("Digite a operação desejada (+, -, *, /):\n")
    num2 = float(input("Insira o segundo número da calculadora:\n"))
    match sinais:
        case '+':
            resultado = num1 + num2
        case '-':
            resultado = num1 - num2
        case '/':
                resultado = num1 / num2
        case '*':
            resultado = num1 * num2
        case _:
            raise ValueError("O símbolo está fora do escopo.")
    print(f"O resultado é: {resultado}")
except ValueError:
    print("Você deve digitar números")
except ZeroDivisionError:
     print("Não se pode dividir por 0.")