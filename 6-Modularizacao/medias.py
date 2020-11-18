""" média, mediana e moda """
from statistics import * #importnto todo o módulo "statistics"

""" funções prontas para o calculo 
-> mean(lista) --> média
-> median(lista) ---> mediana
-> mode(lista) ---> moda
"""

def media(lista):
    # função sun() -> soma os valores do vetor
    media = sum(lista)/float(len(lista))

    return media

def mediana(lista):
    lista.sort()
    t = len(lista)
    
    if t % 2 == 0:
        mediana = (lista[int(t/2)] + lista[int((t/2))-1])/2
    else:
        mediana = lista[int((t/2))]
    
    return mediana

def moda(lista):
    dic = {}
    for i in lista:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    #função max() -->  maior valor
    #método values() --> retorna todos os valores da lista
    maior = max(dic.values())

    for a in dic:
        if dic[a] == maior:
            moda = a
        
        return moda