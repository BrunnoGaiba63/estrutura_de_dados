```python
from lista import Lista


def solicitar_inteiro(texto):
    """Solicita um número inteiro ao usuário."""
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Valor inválido. Informe um número inteiro.")


def mostrar_menu():
    """Mostra na tela as opções disponíveis."""
    print("\n--- Gerenciamento da lista encadeada ---")
    print("1. Adicionar um número inteiro")
    print("2. Excluir a primeira ocorrência de um número")
    print("3. Verificar um número")
    print("4. Limpar a lista")
    print("5. Sair do programa")


def executar():
    """Controla a execução das operações da lista."""
    lista = Lista()

    while True:
        mostrar_menu()
        escolha = input("Digite uma opção: ").strip()

        if escolha == "1":
            numero = solicitar_inteiro("Informe o número para inserir: ")
            lista.inserir(numero)
            print(f"O número {numero} foi adicionado com sucesso.")

        elif escolha == "2":
            numero = solicitar_inteiro("Informe o número para excluir: ")

            if lista.remover(numero):
                print(f"A primeira ocorrência de {numero} foi excluída.")
            else:
                print(f"Não foi encontrado o número {numero} na lista.")

        elif escolha == "3":
            numero = solicitar_inteiro("Informe o número que deseja verificar: ")

            if lista.buscar(numero):
                print(f"O número {numero} está presente na lista.")
            else:
                print(f"O número {numero} não está presente na lista.")

        elif escolha == "4":
            lista.destruir()
            print("A lista foi limpa com sucesso.")

        elif escolha == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opção inválida. Digite uma opção entre 1 e 5.")


if __name__ == "__main__":
    executar()
```
