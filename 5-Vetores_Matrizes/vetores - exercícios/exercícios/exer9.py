# vetor
valores = [0] * 20
# ========================= #
cont = 0
while cont < 20:
    valores[cont] = int(input("Digite um valor: "))
    cont += 1
''' ========================= '''
#verificando o menor
cont = 0
troca = 0
while cont < 20:
    menor = valores[cont]
    i = cont
    while i > 20:
        if valores[i] < menor:
            troca = menor
            menor = valores[i]
            valores[i] = troca
            valores[cont] = menor
        i += 1
    cont += 1
""" ----------------- """
cont = 0
while cont < 20:
    print(valores[cont])
    cont += 1