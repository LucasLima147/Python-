"""
Parecida com a função map(), contudo, é ligeiramente mais rápido. 
Porém, exige um pouco uma abstração melhor do que será processado
    Ela me permite utilizar qualquer expressão arbitrária
    Modo de uso:
        [retorno for variavel in sequencia] -> retorna uma lista
"""
# forma básica
lst_1 = [x for x in 'python']
print("Lista da palavra 'python':", lst_1)

# elevando os valores da lista ao quadrado
lst_2 = [x**2 for x in range(0, 11)]
print("\nLista de algarismos aos quadrado:", lst_2)

# retornando apenas os números pares
lst_3 = [x for x in range(11) if x % 2 == 0]
print("\nLista do números pares:", lst_3)

# retornar a conversão das temperaturas em celcius em fahrenheit
celcius = [0, 10, 20.1, 34.5]
fahrenheit = [((float(9)/5) * temp + 32) for temp in celcius]
print("\nTemperaturas em Celcius {0} \nTemperaturas em fahrenheit {1}".format(celcius, fahrenheit))

# operações aninhadas, list comprehension dentro de outra
lst_4 = [x**2 for x in [x**2 for x in range(0, 11)]]
print("\nLista de algarismos aos quadrado:", lst_4)