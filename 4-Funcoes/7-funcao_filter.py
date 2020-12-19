"""
Esta função é uma forma de usar funções criadas para buscas dentro de uma sequencia
filtrando os elementos que a função retorne True
    Exemplo de uso:
        - Filtro de dados
    Forma de usar:
        filter(funcao, sequencia) -> retornará True ou False em caso de 1 valor ou uma lista dos que forem retornados como True
        não altera a lista original
"""
# Definindo a função que faz o filtro e a lista


def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Exemplo 1: com função criada
print("Lista original:", lista)
print("Com o filter: ", list(filter(verificaPar, lista)))

# Exemplo 2: com função anonima
print("\nLista original:", lista)
print("FIlter com lambda:", list(filter(lambda x: x % 2 == 0, lista)))
