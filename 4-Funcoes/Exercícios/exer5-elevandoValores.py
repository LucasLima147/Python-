# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]

for x in map(lambda a,b: a**b, listaA, listaB):
    print(x)

#########################
print(list(map(pow, listaA, listaB)))           # pow(num1, num2) -> eleva o primeiro número pelo segundo
print(pow(4, 5))