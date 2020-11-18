"""		importações		"""
import random
import os

"""		MODULOS		"""
def busca_serial(vetor, chave, encontradoValor):
	i = 0
	N = len(vetor)
	while (i < N and chave != vetor[i]):
	 	i += 1

	encontrado = 0
	if i < N:
		encontrado = 1
		if i == 0:
			i += 1

	encontradoValor[0] = encontrado
	return i


def busca_sequencial(vetor, chave, encontradoValor):
	i = 0
	N = len(vetor)
	while (i < N and chave > vetor[i]):
	 	i += 1

	encontrado = 0
	if i < N and chave == vetor[i]:
		encontrado = 1
		if i == 0:
			i += 1
	else:
		i += 1

	encontradoValor[1] = encontrado
	return i


def busca_binaria(vetor, chave, encontradoValor):
	li = 1
	ls = len(vetor)
	meio = ((li+ls)//2)
	qtd_comparacoes = 1
	print(meio)
	while (ls >= li and chave != vetor[meio-1]):
		if chave < vetor[meio-1]:
			ls = meio - 1
		else:
			li = meio + 1
		
		meio = (li+ls)//2
		print(vetor[meio-1], ls, li, meio)
		qtd_comparacoes += 1 
	
	posicao_chave = 0
	if ls >= li:
		posicao_chave = 1
	else:
		qtd_comparacoes -= 1

	encontradoValor[2] = posicao_chave
	return qtd_comparacoes 


def busca_diretaTransformada(vetor, chave, encontradoValor):
	kmenor = vetor[0]
	N = len(vetor)-1
	kmaior = vetor[N]
	Den = kmaior-kmenor
	cte1 = (kmaior-N*kmenor) / Den 
	cte2 = (N-1)/Den
	qtd_comparacoes = 0

	fim = int(cte1+chave*cte2)
	if 1 <= fim <= N and chave != vetor[fim]:
		if chave < vetor[fim]:
			while (fim > 1 and chave < vetor[fim]):
				fim -= 1
				qtd_comparacoes += 1
		else:
			while (fim < N and chave > vetor[fim]):
				fim += 1
				qtd_comparacoes += 1

	posicao_chave = 0
	if (0 <= fim <= N) and (chave == vetor[fim]):
		posicao_chave = 1
	elif chave == vetor[0]:
		posicao_chave = 1

	encontradoValor[3] = posicao_chave
	return qtd_comparacoes+1


def criar_vetor():
	'''tam_vetor = 100
	vetor = [0] * tam_vetor
	cont = 0
	while cont < tam_vetor:
		valor = random.randint(0,1000)
		vetor[cont] = valor
		cont += 1

	vetor.sort()'''
	vetor = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
	return vetor

def listar_vetor(vetor):
	print("Os 20 primeiros números do vetor são: ")
	cont = 0
	while cont < 20:
		print(str(vetor[cont]))
		cont += 1

def relatorio_buscas(resultados):
	print("RELAÇÃO DOS TESTES (registros):\n")
	print(" Chave     Resultado     Serial     Sequencial     Binário     Direta Transformada")	
	for result in resultados:
		print("   {0}          {1}           {2}            {3}            {4}               {5}".format(result[0], result[1], result[2], result[3], result[4], result[5]))

	print("\n\nAnálise de Desempenho:\n")
	linhas = len(resultados)
	# [serial, sequencial, binario, direta transformada]
	totais_comparacoes = [0,0,0,0]
	cont_comparacoes = -1
	for coluna in range(2,6):
		cont_comparacoes += 1
		soma_comparacoes = 0
		for linha in range(linhas):
			soma_comparacoes += resultados[linha][coluna]

		totais_comparacoes[cont_comparacoes] = soma_comparacoes

	print("                        Comparações        Média de Comparações")
	print("Serial                      {0}                   {1}".format(totais_comparacoes[0], (totais_comparacoes[0]/linhas)))
	print("Sequencial                  {0}                   {1}".format(totais_comparacoes[1], (totais_comparacoes[1]/linhas)))
	print("Binário                     {0}                   {1}".format(totais_comparacoes[2], (totais_comparacoes[2]/linhas)))
	print("Direta Transformada         {0}                   {1}".format(totais_comparacoes[3], (totais_comparacoes[3]/linhas)))

#################################################

"""		MAIN	"""
tabela = criar_vetor()
# matriz aonde será guardado a chave, o resultado e o número de comparações de cada função
resultados = []
# linha de cada matriz
# [chave, resultado, serial, sequencial, binaria, diretaTransformada]  
sair = False
while not sair:
	os.system("cls")
	print("******* BUSCA EM TABELAS *******")
	print("Escolha o que deseja fazer")
	print("1 - Criar um novo vetor")
	print("2 - Realizar buscas")
	print("3 - Relatório de Desempenho")
	print("4 - Listar Vetor")
	print("5 - sair")
	opcao = int(input("\nDigite uma opcao do menu: "))

	if opcao == 1:
		tabela = criar_vetor()
		print("vetor criado")
		os.system("pause")

	elif opcao == 2:
		chave = int(input("\ndigite o valor procurado: "))
		encontradoValor = [0]*4
		# [chave, resultado, serial, sequencial, binaria, diretaTransformada]
		busca = [chave, 0, busca_serial(tabela, chave, encontradoValor),
				busca_sequencial(tabela, chave, encontradoValor), 
				busca_binaria(tabela, chave, encontradoValor), 
				busca_diretaTransformada(tabela, chave, encontradoValor)]
		
		# verificando se alguma função não encontrou o valor
		# link sobre a função any() e all(): https://pythonhelp.wordpress.com/2012/11/06/all-e-any/
		if any(result == 0 for result in encontradoValor):
			print("nem todas as funções encontraram a chave procurada")
			print(encontradoValor)
		else:
			print("todas as funções encontraram a chave procurada")
			busca[1] = 1
		
		resultados.append(busca)
		os.system("pause")
	elif opcao == 3:
		relatorio_buscas(resultados)
		os.system("pause")
	elif opcao == 4:
		listar_vetor(tabela)
		os.system("pause")
	elif opcao == 5:
		sair = True
	else:
		print("opção inválida")
		os.system("pause") 