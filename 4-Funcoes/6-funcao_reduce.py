"""
Diferente da função map() que aplica a função a cada elemento da lista e devolve uma nova lista,
a função reduce() aplica a função a cada elemento da lista, mas devolvendo um único valor no final
    Exemplo de uso:
        - somar todos os elementos de uma lista
    Forma de usar:
        from functools import reduce 
        reduce(funcao, sequencia)
        a sequencia original não será alterada
"""
# importando o reduce
from functools import reduce

# criando função e a lista
def soma(a, b):
    x = a + b
    return x
lista = [47, 11, 42, 13]

# Exemplo 1: com a função criada
print("Reduce com função craida:", reduce(soma, lista))

# Exemplo 2: com a função anonima
print("Reduce com função anonima:", reduce(lambda x, y: x+y, lista))

# Exemplo 2: com a função anonima com condição
"Uma forma de ver o maior valor da lista"
maior_valor = lambda a, b: a if(a > b) else b

print(type(maior_valor))
print("Reduce com função anonima com condição:", reduce(maior_valor, lista))