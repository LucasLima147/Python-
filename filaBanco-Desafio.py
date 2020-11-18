import random
from os import system

#Variáveis
fila = []
caixa1 = 0
caixa2 = 0
caixa3 = 0
cliente = 0
Maior_fila = 0

#Variáveis para as horas
horas = 8
minutos = 00


while True:
	system("cls")

	if minutos < 60:
		minutos += 1
	else:
		if (horas+1) == 22:
			horas = 0
			minutos = 0
		else:
			horas += 1
			minutos = 00

	print("Maior fila até agora: {0} Pessoas as {1}h e {2}min".format(Maior_fila,horas,minutos))
	print("O caixa 1 já atendeu: {0} Pessoas".format(caixa1))
	print("O caixa 2 já atendeu: {0} Pessoas".format(caixa2))
	print("O caixa 3 já atendeu: {0} Pessoas".format(caixa3))
	print(fila)

	opcao = random.randint(0,20)
	if 0 <= opcao < 9:
		cliente += 1
		fila.append(cliente)
		if len(fila) > Maior_fila:
			Maior_fila = len(fila)
	elif 9 <= opcao < 13:
		if len(fila) != 0:
			caixa1 += 1
			fila.pop(0)
	elif 13 <= opcao < 16:
		if len(fila) != 0:
			caixa2 += 1
			fila.pop(0)
	elif 16 <= opcao < 20:
		if len(fila) != 0:
			caixa3 += 1
			fila.pop(0)
	elif opcao == 20:
		desejo = input("Deseja continuar?[s/n]   ")
		if desejo == "n":
			system("pause")
			break