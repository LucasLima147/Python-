lista1 = ["abacate", "melancia", "abacaxi", "maça", "peixe"]
lista2 = [1, 2, 3, 4, 5]
lista3 = ["abacaxi", 1, 9.98, True]

print("TAMANHO DO VETOR")
tamanho = len(lista2)
print(tamanho, "\n")


print("ADICIONANDO ITENS AO VETOR")
print("lista original", lista1)
lista1.append("limao")
print("lista com valor adicionado\n", lista1, "\n") 

print("VERIFICANDO SE DETERMINADO VALOR EXISTE NA LISTA")
# uso a palavra reservada "in"
if 3 in lista2:
    print("3 está na lista", "\n")

# uso a palavra reservada "del"
print("REMOVENDO ITENS DA LISTA")
print("lista original:", lista1)
del lista1[1:3]
print("lista com valores removidos:", lista1, "\n")

""" ======================================= """
print("ORDENANDO UMA LISTA: CRESCENTE")
vetor = [124,345,5,72,46,6,7,3,1,7,0]
vetor2 = [124,345,5,72,46,6,7,3,1,7,0]
#duas formas para se ordenar uma lista
#método sort() -> altera uma lista sem precisar armazenar em uma variável
print("lista original 1 ->", vetor)
vetor.sort()
print("método sort()->", vetor, "\n")

#função sorted() ordena a lista mas precisa ser armazenada em uma variável
print("ORDENANDO UMA LISTA: DECRESCENTE")
print("lista original 2 ->", vetor2)
ordenada = sorted(vetor2)
print("função 2 sorted()->", ordenada)
#posso ainda usar outro modo
print("vetor base ->", vetor)
vetor.sort(reverse=True)
print("método sort(reverse=True) ->", vetor, "\n")


print("INVERTENDO OS VALORES")
print("vetor base ->", vetor2)
vetor2.reverse()
print("método reverse() ->", vetor2, "\n")

print("ORDEM ALFABÉTICA")
lista = ["abacate", "melancia", "abacaxi", "beijo", "zebra", "tentáculo"]
print("lista base ->", lista)
lista.sort()
print("método sort() ->", lista)
lista.sort(reverse=True)
print("método sort(reverse=True) ->", lista, "\n")

""" ======================================= 
Vejamos algumas funções com vetores interessantes
"""
teste = [3, 2, 9, 1, 1, 2, 3, 1, 8]

print("VERIFICANDO QUANTAS VEZES UM ELEMENTO SE REPETE")
#método count(elemento) -> quantas vezes um elemento se repete
print(f"O número 1 repete {teste.count(1)} vezes, e o número 2 repete {teste.count(2)} vezes \n")


'''
método index()
mostra a posição aonde se encontra a PRIMEIRA aparição de um elemento

existem 3 formas:
->1. só passando um elemento
lista.index(elemento) ---> busca na lista toda
->2. a partir de determinada posição
lista.index(elemento, posição inicial de busca)
->3. de uma posição, até a outra
lista.index(elemento, posição inicial de busca, posição final de busca)
'''
print("ACHANDO A POSIÇÃO DE UM VALOR NA LISTA")

#1
print("A primeira aparição do numero 9 é na posição:", teste.index(9))
#2
print("Depois da 2º posição , o número 2 aparece na posição", teste.index(2, 2))
#3
print("Entre a posição 2 e 8, o número 3 aparece na posição", teste.index(3, 2, 8))