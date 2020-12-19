"""
possibilita unir 2 sequencias (Ex: 2 listas) e retorna uma tupla
    OBS: Se uma sequência for menor que a outra, ele vai retornar o número de tuplas da menor sequencia
    Forma de uso:
        zip(sequencia_1, sequencia_2)
"""
# Unindo listas de tamanhos iguais e mesmo tipo
lst = list(zip([1, 2, 3,], [5, 6, 7]))                  # retorna um objeto, por isso usamos list()
print("União de duas listas de tamanhos iguas:", lst)

# Unindo listas de tamanhos diferentes e mesmo tipo
lst = list(zip("ABCD", "xy"))                            # atenção quando as sequencias de tamanho diferente
print("\nUniãõ de duas listas de tamanhos diferentes:", lst)

# Unindo listas de tipos diferentes
lst = list(zip("ABCD", [1, 2, 3, 4]))                            # atenção quando as sequencias de tamanho diferente
print("\nUniãõ de duas listas de tipos diferentes:", lst)

# Unindo dicionários
d1 = {"a": 2, "b": 4}
d2 = {"x": 5, "y": 6}
lst = list(zip(d1, d2))                                         # seá unido somento os valores das chaves
print("\nSó colocando os dicionários (sem o .values()):", lst)  # desconsiderou os valores
# trocando os valores de um dos discionários
lst = list(zip(d1, d2.values()))                                # agora usando o .values()
print("Só colocando os dicionários (com o .values()):", lst)    # colocou o valor de um dos dicionários


""" TROCANDO OS VALORES DE UM DOS DICIONÁRIOS """
def trocaValor(dic1, dic2):
    # craindo um dicionário vazio
    dicTmp = {}
    # separando as chaves e valores para o dicionário
    for d1key, d2val in zip(dic1, dic2.values()):
        # adicionando a chave o valor da chave no dicionário vazio
        dicTmp[d1key] = d2val
    # retornando o dicionário
    return dicTmp

print("\ndicionário 1: {0} | {1}".format(d1.keys(), d1.values()))
print("dicionário 2: {0} | {1}".format(d2.keys(), d2.values()))
d3 = trocaValor(d1, d2)
print("valores trocados:{0} | {1}".format(d3.keys(), d3.values()))