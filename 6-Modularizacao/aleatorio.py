""" criando uma lista com números aleatórios """
import random

#parametro "tam" vem do valor que foi passado no arquivo main.py
def criaraleatorio(tam):
    lista = [] #lista vazia
    for i in range(tam):
        #gerando valores aleatórios e guardando na lista
        lista.append(random.randint(0, tam))
    
    #retornando ao main.py
    return lista