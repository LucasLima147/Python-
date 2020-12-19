'''
    map(função, sequencia_interalvel) -> aplica a função a cada elemento da sequencia (Ex: lista)
        -> Ele irá retornar um 'interator', então devemos usar a função list(
                isso irá converter o interator em lista para manipulação
        -> observado que a lista original usado no map não foi alterada 
'''
# DEFININDO AS FUNÇÕES E LISTA DE TEMPERATURA
# Converter a temperatura em Fahrenheit


def fahrenheit(t):
    return ((float(9) / 5) * t + 32)

# Converter a temperatura em Celsius


def celsius(t):
    return ((float(5) / 9)) * (t - 32)


# Temperaturas
temps = [0, 22.5, 40, 100]
# ==============================================
# PRIMEIRA FORMA DE UTILIZAR A FUNÇÃO map()
print("Forma 1 de usar o map()\n")
temp_fahrenheit = list(map(fahrenheit, temps))
print("Lista original:", temps)
print("Nova lista:", temp_fahrenheit)

# SEGUNDA FORMA DE UTILIZAR A FUNÇÃO map()
print("\nForma 2 de usar o map()")
print("Lista Original:", temps)
for fah in map(celsius, temps):
    print(fah)
print("Lista pós o for", temps)

# TERCEIRA FORMA DE UTILIZAR A FUNÇÃO map()
print("\nForma 3 de usar o map()")
print("Lista Original:", temps)
lista_lambda = list(map(lambda x: (5.0 / 9) * (x - 32), temps))
print("Lista Lambda:", lista_lambda)

# QUARTA FORMA DE UTILIZAR A FUNÇÃO map()
print("\nForma 4 de usar o map()")
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]
print("Listas originais: {0} {1} {2}".format(a, b, c))

lista_lambda = list(map(lambda x, y: x+y, a, b))
print("Lista gerada com o lambda (2 listas):", lista_lambda)

lista_lambda = list(map(lambda x, y, z: x+y+z, a, b, c))
print("Lista gerada com o lambda (3 listas):", lista_lambda)
