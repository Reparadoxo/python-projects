import random

def gerarSenha():
    maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "123456789"
    especiais_comuns = "&%$#@!*-/_"
    caracteres_finais = maiusculas + minusculas + numeros + especiais_comuns

    senha = [
        random.choice(maiusculas), 
        random.choice (minusculas), 
        random.choice(numeros), 
        random.choice(especiais_comuns)
    ]

    senha.extend(random.choices(caracteres_finais, k=8))

    random.shuffle(senha)

    return ''.join(senha)

senha = gerarSenha()

print(f"A senha gerada é: {senha}\nLembre-se de não compartilhar com outras pessoas!")
