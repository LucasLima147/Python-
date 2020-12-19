"""
A função enumerate() nos retornar tuplas com o indice do valor e o valor dentro de uma sequencia
"""
nome = ["L", "u", "c", "a", "s"]                           # String -> posso separar em uma lista ..$
ind = list(enumerate(nome))                                # retorna um objeto, por isso usamos o list()
print("Indices e valores (separado):", ind)

ind = list(enumerate("Lucas"))                          # $.. ou posso somente passar ela sem separar
print("\nIndices e valores (sem separar):", ind)

# Usando o for para pegar o indice e o valor
print("\nListando os indicies e valores (respectivamente) com o for:")
for indice, valor in enumerate(nome):
    print("", indice, valor)

# Usando o for para pegar o indice e o valor até um indice especifico
print("\nListando os valores até o indice 2 com o for:")
for indice, valor in enumerate(nome):
    if indice >= 2:
        break
    else:
        print("", indice, valor)