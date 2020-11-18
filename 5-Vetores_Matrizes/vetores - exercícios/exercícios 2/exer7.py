valor = [0] * 10
pecas = [0] * 10
##########
cont = 0
while cont < 10:
    pecas[cont] = int(input("digite o  numero de pecas: "))
    valor[cont] = float(input(("Digite o valor dessa peca: ")))
    cont += 1
########
totalpecas = 0
for i in pecas:
    totalpecas += i
print("total de pecas: ", totalpecas)
########
i = 0
while i < 10:
    print("o valor total da peca", i, " é: ", pecas[i] * valor[i])
    i += 1