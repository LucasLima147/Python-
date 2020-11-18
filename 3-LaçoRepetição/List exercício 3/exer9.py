from math import sqrt

raiz = sqrt(int(input("Digite um valor para a Raiz Quadrada: ")))
num = 0
while raiz > 1:
    num = num + 1
    raiz = raiz - 1

if raiz >= 0.5:
    num = num + 1
print(num)