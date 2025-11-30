import os

def limpar_tela():
    """Função auxiliar para limpar o console."""
    os.system('cls')

def adicionarTarefa(lista):
    limpar_tela()
    tarefa = input("Digite a tarefa que você deseja adicionar na lista:\n")
    lista.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
    return lista

def visualizarTarefas(lista):
    limpar_tela()
    if not lista:
        print("Sua lista de tarefas está vazia.")
    else:
        print("--- Suas Tarefas ---")
        for indice, item in enumerate(lista):
            print(f"{indice}: {item}")
        print("--------------------")
    input("\nPressione Enter para continuar...")

def removerTarefa(lista):
    limpar_tela()
    if not lista:
        print("Não há itens para remover na lista.")
        input("Pressione Enter para continuar...")
        return lista

    print("Itens da lista atuais:\n")
    for indice, item in enumerate(lista):
        print(f"{indice}: {item}")
    
    try:
        excluir = int(input(f"\nInsira o NÚMERO da tarefa (0 a {len(lista)-1}) que você deseja excluir:\n"))
        
        if excluir < 0 or excluir >= len(lista):
            print(f"ERRO: Número inválido! Insira um valor entre 0 e {len(lista)-1}.")
            input("Pressione Enter para retornar ao menu...")
            return lista
        
        item_removido = lista.pop(excluir)
        confirmacao = input(f"Você está excluindo '{item_removido}'.\nTem certeza que quer continuar? (S/N): ").lower()
        
        if confirmacao == 's':
            print(f"Item '{item_removido}' removido permanentemente.")
            input("Pressione Enter para retornar ao menu...")
            return lista
        else:
            lista.insert(excluir, item_removido)
            print("Item restaurado. Nada foi alterado.")
            input("Pressione Enter para retornar ao menu...")
            return lista
            
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
        input("Pressione Enter para retornar ao menu...")
        return lista

def sair():
    limpar_tela()
    confirmacao_sair = input("Tem certeza que deseja sair? (S/N): ").lower()
    if confirmacao_sair == "s":
        print("Saindo do programa. Até mais!")
        exit()
    elif confirmacao_sair == "n":
        return False 
    else:
        print("Sinal não reconhecido. Retornando ao menu.")
        return False

# --- LOOP PRINCIPAL DO PROGRAMA ---

def main():
    # A lista é inicializada aqui e passada para as funções
    lista_tarefas = []
    
    while True:
        limpar_tela()
        try:
            escolha = int(input(f"""Bem vindo ao gerenciador de tarefas!
Atualmente você tem {len(lista_tarefas)} tarefas.
          \nEscolha uma opção:\n
          1. Adicionar tarefa\n
          2. Visualizar tarefas\n
          3. Remover tarefa\n
          4. Sair\n\n"""))
            
            match escolha:
                case 1:
                    adicionarTarefa(lista_tarefas)
                case 2:
                    visualizarTarefas(lista_tarefas)
                case 3:
                    removerTarefa(lista_tarefas)
                case 4:
                    if sair():
                        break # Sai do loop while True
                case _:
                    print("Opção fora do escopo. Tente novamente.")
                    input("Pressione Enter para continuar...")
        
        except ValueError:
            print("Entrada inválida. Digite um número de 1 a 4.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
