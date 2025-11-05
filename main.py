valorConta = float(input("Digite o valor da sua conta: \n"))

porcentagemGorjeta = float(input("Qual a porcentagem da sua gorjeta? \n"))

contaFinal = valorConta + (valorConta * (porcentagemGorjeta / 100))

print(f"O valor da sua conta total é: R${contaFinal:.2f} reais")
print(f"O valor da sua gorjeta é: R${porcentagemGorjeta:.2f} reais")