N = 12 
temp = [0] * 12 
maior = 0.0
menor = 0.0 

# primeiro mes deve ser lido seprado para atribuir a maior e a menor temperatura do momemto
temp[0] = float(input("Digite a temperatura do mes de janeiro: "))
maior = temp[0]
menor = temp[0]
""" MAIORES E MENORES TEMPERATURAS """
cont = 1
while cont < N:
    temp[cont] = float(input("Digite a temperatura do proximo mes: "))
    if temp[cont] >= maior:
        maior = temp[cont]
    elif temp[cont] <= menor:
        menor = temp[cont]
    cont += 1
""" MESES DA MAIORES E MENORES TEMPERATURAS """
cont = 0
while cont < N:
    if temp[cont] == maior:
        print("meses das maiores temperaturas: ", cont + 1)
    cont += 1
 #-----------------#
cont = 0
while cont < N:
    if temp[cont] == menor:
        print("meses das menores temperaturas: ", cont + 1)
print(maior, menor)
