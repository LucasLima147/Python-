# Vetor
valores = [0] * 20
""" ------------------------- """
cont = 0 
while cont < 20:
    valores[cont] = int(input("Digite um valor: "))
    cont += 1
""" ========================= """
cont = 0 
troca = 0
while cont < 20:
    menor = valores[cont]
    i = 19
    while i > cont:
        if valores[i] < menor:
            troca = menor
            menor = valores[i]
            valores[i] = troca
            valores[cont] = menor
        i -= 1
    cont += 1
""" -------------------------- """
cont = 0
while cont < 20:
    print(valores[cont])
    cont += 1