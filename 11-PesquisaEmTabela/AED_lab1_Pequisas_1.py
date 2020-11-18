"""		importações		"""
import random
import os

"""		MODULOS		"""
def busca_serial(vetor, chave):
	i = 0
	N = len(vetor)
	while (i < N and chave != vetor[i]):
	 	i += 1

	posicao_chave = -1
	if i < N:
		posicao_chave = i

	return posicao_chave


def busca_sequencial(vetor, chave):
	i = 0
	N = len(vetor)
	while (i < N and chave > vetor[i]):
	 	i += 1

	posicao_chave = -1
	if i < N and chave == vetor[i]:
		posicao_chave = i

	return posicao_chave


def busca_binaria(vetor, chave):
	li = 0
	ls = len(vetor)
	meio = (li+ls)//2
	while (ls >= li and chave != vetor[meio]):
		if chave < vetor[meio]:
			ls -= 1
		else:
			li += 1

		meio = (li+ls)//2

	posicao_chave = -1
	if ls >= li:
		posicao_chave = meio

	return posicao_chave 


def busca_diretaTransformada(vetor, chave):
	kmenor = vetor[0]
	N = len(vetor)-1
	kmaior = vetor[N]
	Den = kmaior-kmenor
	cte1 = (kmaior-N*kmenor) / Den 
	cte2 = (N-1)/Den

	fim = int(cte1+chave*cte2)
	if 1 <= fim <= N and chave != vetor[fim]:
		
		if chave < vetor[fim]:
			while (fim > 1 and chave < vetor[fim]):
				fim -= 1
		else:
			while (fim < N and chave > vetor[fim]):
				fim += 1

	posicao_chave = -1
	if (0 <= fim <= N) and (chave == vetor[fim]):
		posicao_chave = fim
	elif chave == vetor[0]:
		posicao_chave = 0

	return posicao_chave


def criar_vetor():
	tam_vetor = 20
	vetor = [0] * tam_vetor
	cont = 0
	while cont < tam_vetor:
		valor = random.randint(0,1000)
		vetor[cont] = valor
		cont += 1

	vetor.sort()
	return vetor

def listar_vetor(vetor):
	print("Os 20 primeiros números do vetor são: ")
	cont = 0
	for valor in vetor:
		print(str(valor))

#################################################

"""		MAIN	"""
tabela = criar_vetor()
sair = False
while not sair:
	os.system("cls")
	print("******* BUSCA EM TABELAS *******")
	print("Escolha o que deseja fazer")
	print("1 - Criar um novo vetor")
	print("2 - Busca Serial")
	print("3 - Busca Sequencial")
	print("4 - Busca busca_binaria")
	print("5 - Busca Direta Transfornada")
	print("6 - Listar Vetor")
	print("7 - sair")
	opcao = int(input("\nDigite uma opcao do menu: "))

	if opcao == 1:
		tabela = criar_vetor()
		print("vetor criado")
		os.system("pause")
	elif opcao == 2:
		chave = int(input("Digie o valor a ser procurado: "))
		posicao_chave = busca_serial(tabela, chave)
		if(posicao_chave != -1):
			print("esse valor está na posicao: "+str(posicao_chave+1))
		else:
			print("valor não encontrado")
		os.system("pause")
	elif opcao == 3:
		chave = int(input("Digie o valor a ser procurado: "))
		posicao_chave = busca_sequencial(tabela, chave)
		if(posicao_chave != -1):
			print("esse valor está na posicao: "+str(posicao_chave+1))
		else:
			print("valor não encontrado")
		os.system("pause")
	elif opcao == 4:
		chave = int(input("Digie o valor a ser procurado: "))
		posicao_chave = busca_binaria(tabela, chave)
		if(posicao_chave != -1):
			print("esse valor está na posicao: "+str(posicao_chave+1))
		else:
			print("valor não encontrado")
		os.system("pause")
	elif opcao == 5:
		chave = int(input("Digie o valor a ser procurado: "))
		posicao_chave = busca_diretaTransformada(tabela, chave)
		if(posicao_chave != -1):
			print("esse valor está na posicao: "+str(posicao_chave+1))
		else:
			print("valor não encontrado")
		os.system("pause")
	elif opcao == 6:
		listar_vetor(tabela)
		os.system("pause")
	elif opcao == 7:
		sair = True
	else:
		print("opção inválida")
		os.system("pause") 