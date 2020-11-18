lista = ["roberto", '52', "fai", '1500.00']
lista.append("lucas")               # adiciona um item no final da lista
lista.insert(1,"Erika")             # adiciona um valor na lista com vase na posição escolhida
lista.remove("fai")                 # remove um valor de uma lista
lista.sort()                        # ordena os valores da lista
lista.extend(vetor)                # adiciona os valores de uma lista no final de outra lista

vetor = lista.copy()                # copia a lista em outra variável
qtd_valor = lista.count(52)         # conta quantas vezes um valor repete na lista
valor = lista.pop(4)                # tira um valor da lista e salva na variável
print(lista.index(valor), lista)    # retorna a posição de um valor na lista