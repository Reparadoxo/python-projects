def validarCPF(cpf):
    if cpf.isdigit() == True:
        if len(cpf) == 11:
            print("O seu CPF foi aceito.")
        else:
            print("O seu CPF foi inserido incorretamente, ele deve conter 11 caracteres.")
    else: 
        print("O seu CPF deve conter apenas números.")

cpf = str(input("Digite o seu CPF!\n"))

validarCPF(cpf)