''' Número aeatórios '''
import random #importaão dos méodos

""" método randint(de, até) -> sortear um número dentro de uma faixa """
num = random.randint( 0, 10)
print(num)

""" método choice(list) -> sortea um número de uma lista """
lista = [0, 34, 59, 14]
num = random.choice(lista)
print(num)