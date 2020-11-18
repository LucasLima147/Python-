cont = 0
maior = 0
index = 0

while cont < 10:
    valor = int(input())
    if valor > maior:
        maior = valor
        index = cont+1
    cont += 1

print(maior)
print(index)