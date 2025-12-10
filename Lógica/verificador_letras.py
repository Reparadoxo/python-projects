def verificarPalavraLonga(texto):
    palavraGrande = []
    for palavra in texto.split(): #split divide uma palavra pelos seus espaços
        if len(palavra) >= 10:
            palavraGrande.append(palavra)
            print(f"Uau, a palavra '{palavra}' é bem grande!")
        else:
            print(f"A palavra '{palavra}' não é tão grande.")
    
    if len(palavraGrande) >= 1:
        print(f"As palavras grandes são: ")
        for palavras in palavraGrande:
            print(f"{palavras}\t")
    else:
        print("Esse texto não tem textos longos.")
    

texto = str(input("Insira um texto para verificarmos as palavras dele: \n"))

verificarPalavraLonga(texto)