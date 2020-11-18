valor = [0] * 10
pecas = [0] * 10
##########
cont = 0
while cont < 10:
    pecas[cont] = int(input("digite o  numero de pecas: "))
    valor[cont] = float(input(("Digite o valor dessa peca: ")))
    cont += 1
########
i = 0
while i < 10:
    print("o valor total da peca", i, " é: ", pecas[cont] * valor[cont])
    i += 1