def main():
    estoque1 = tuple(input("Produtos do estoque 1: \n").split(", "))
    estoque2 = tuple(input("Produtos do estoque 2: \n").split(", "))
    print(f"O estoque1: {estoque1}\t O estoque2: {estoque2}")
    estoqueCombinado = estoque1 + estoque2
    print(f"Estoque combinado: {estoqueCombinado}")

if __name__ == "__main__":
    main()