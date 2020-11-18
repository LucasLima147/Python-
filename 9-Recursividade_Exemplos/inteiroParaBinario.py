#IMPORTAÇÃO
from os import system

# Procedimento Push
def PUSH(p, valor):
	if p["topo"] == 32:
		print("Pilha cheia")
	else:
		p["topo"] += 1
		p["elementos"][p["topo"]-1] = valor

# Procedimento Pop
def POP(p):
	if p["topo"] == 0:
		print("Pilha Vazia")
		valor = -1
	else:
		valor = p["elementos"][p["topo"]-1]
		p["topo"] -= 1

	return valor

def DECIMAL_BINARIO(NUMERO):
	N = 32
	pilha= {"topo":0, "elementos":[0]*N}

	while NUMERO != 0:
		aux = NUMERO % 2
		PUSH(pilha, aux)
		NUMERO = NUMERO // 2

	while pilha["topo"] != 0:
		aux = POP(pilha)
		print(aux)

# MAIN
print("Vamos converter números INTEIROS em Binários")
valor = 5
while valor >= 1:
	system("cls")
	
	print("o numero {0} em binário é: ".format(valor))
	DECIMAL_BINARIO(valor)
	print("\n")
	valor = int(input("Digite outro valor INTEIRO para convertermos ou qualquer valor menor que 1 para sair do programa:"))

print("Obrigado por usar nosso programa")
system("pause")