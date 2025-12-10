def contarVogais(frase):
    vogais = "aeiou"
    espaco = " "
    contagemVogais = 0
    contagemConsoante = 0
    contagemEspaco = 0
    for letras in frase.lower(): #lower manipula as letras para ficarem minúsculas
        if letras in vogais:
            contagemVogais += 1
            print(f"A letra {letras} é vogal.")
        elif letras in espaco: 
            print("Aqui teve um espaço :)")
            contagemEspaco += 1
        else:
            print(f"A letra {letras} é uma consoante.")
            contagemConsoante += 1
    return contagemVogais, contagemConsoante, contagemEspaco

frase = str(input("Digite uma frase sem acentos para contarmos as consoantes e as vogais: \n"))

contagemVogais, contagemConsoante, contagemEspaco = contarVogais(frase)

print(f"A sua frase tem {contagemVogais} vogais e {contagemConsoante} consoantes e {contagemEspaco} espaços em branco.")