#Numero N de vaores a serem lidos
N = int(input("digite o numero de valores a serem lidos: "))
valores = [0] * N
#Salvando cada valor no vetor
cont = 0
while cont < N:
	valores[cont] = int(input("Digite um numero: "))
	cont += 1
"""------------------------"""
#verificando se é numero primo e sua posição
cont = 0
while cont < N:
	divisor = 1
	primo = 0
	while divisor <= valores[cont]:
		if (valores[cont] % divisor) == 0:
			primo += 1
		divisor += 1
	#Verificando se é primo
	if primo == 2:
		print(valores[cont], " é um numero primo")
		print("Sua posição no vetor é: ", cont)
	cont += 1