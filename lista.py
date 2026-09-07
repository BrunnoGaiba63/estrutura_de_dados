```python
class _No:
    """Representa um elemento interno da lista encadeada."""

    def __init__(self, valor):
        """Cria o nó armazenando um inteiro e sem próximo elemento."""
        self.__valor = valor
        self.__seguinte = None

    def obter_valor(self):
        """Retorna o valor guardado no nó."""
        return self.__valor

    def obter_proximo(self):
        """Retorna o próximo elemento ligado ao nó."""
        return self.__seguinte

    def definir_proximo(self, proximo):
        """Estabelece qual será o próximo nó."""
        self.__seguinte = proximo


class Lista:
    """Representa uma lista simplesmente encadeada de números inteiros."""

    def __init__(self):
        """Cria uma lista inicialmente vazia."""
        self.__inicio = None

    @staticmethod
    def __validar_valor(valor):
        """Verifica se o valor informado é um inteiro."""
        if type(valor) is not int:
            raise TypeError("O valor precisa ser um número inteiro.")

    def inserir(self, valor):
        """Adiciona um novo valor ao final da lista."""
        self.__validar_valor(valor)
        novo = _No(valor)

        if self.__inicio is None:
            self.__inicio = novo
            return

        atual = self.__inicio
        while atual.obter_proximo() is not None:
            atual = atual.obter_proximo()

        atual.definir_proximo(novo)

    def remover(self, valor):
        """Exclui a primeira ocorrência encontrada e retorna o resultado."""
        self.__validar_valor(valor)

        anterior = None
        atual = self.__inicio

        while atual is not None:
            if atual.obter_valor() == valor:
                seguinte = atual.obter_proximo()

                if anterior is None:
                    self.__inicio = seguinte
                else:
                    anterior.definir_proximo(seguinte)

                atual.definir_proximo(None)
                return True

            anterior = atual
            atual = atual.obter_proximo()

        return False

    def buscar(self, valor):
        """Verifica se determinado valor está presente na lista."""
        self.__validar_valor(valor)

        atual = self.__inicio

        while atual is not None:
            if atual.obter_valor() == valor:
                return True

            atual = atual.obter_proximo()

        return False

    def destruir(self):
        """Remove as ligações entre os nós e esvazia a lista."""
        atual = self.__inicio
        self.__inicio = None

        while atual is not None:
            seguinte = atual.obter_proximo()
            atual.definir_proximo(None)
            atual = seguinte
```
