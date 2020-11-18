'''
O CÓDIGO SERÁ O MESMO TANTO PARA O ARQUIVO .fasta DA BACTERIA E DO HUMANO
### O QUE MUDA... ###
--> bacteria: 
		entrada = open("16s_bacteria.fasta").read(
		saida = open("16s_bacteria.html","w")
--> humano:
		entrada = open("18s_humano.fasta").read()
		saida = open("18s_humano.html","w")
'''

#pegando o arquivo.fasta da bacteria e lendo o arquivo
entrada = open("18s_humano.fasta").read()
#arquivo html que será gerado para o comparativo
saida = open("18s_humano.html","w")

#dicionário para contagem
cont = {}

'''
FORs para gerar o dicionário onde:
->combinações de i+j geram as chaves
->todos os valores serão 0
'''
for i in ['A', 'T', 'C', 'G']:
	for j in ['A', 'T', 'C', 'G']:
		cont[i+j] = 0

#o arquivo contem uma quebra de linha, por isso, devemos removela
# ->usaremso o método replace para substituir a quebra por um espaço
entrada = entrada.replace("\n","")

#fazendo a contagem de cada par gerados no for acima 
#sendo o último elemento sem par
for k in range(len(entrada)-1):
	'''
	entrada[k]+entrada[k+1]
	->concatena caracter que estiver na prosicao K, mais o proximo(K+1)
	
	cont[]
	->o resultado retornado da soma das entradas será uma combinação
	->verifica qual chave a combiação representa
	->o valor da chave que for representada, será somado +1
	'''
	cont[entrada[k]+entrada[k+1]] += 1

'''
===========================================
			GERANDO O HTML 
'''
saida.write("<div>")

#contador
i = 1

#varendo os resultados do cont
for k in cont:

	#nível de transparencia
	transparencia = cont[k]/max(cont.values())
	#escrevendo as DIVs no arquivo HTML com um nível de transparencia
	# ->isso é feito de acordo com a quantidade de cada combinacao
	saida.write(f"<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color:rgba(0, 0, 0, {str(transparencia)}')>{k} = {cont[k]}</div>")

	#"quebra de linha" a cada 4 blocos
	#isso acontece quando o contador for divivel por 4
	if i%4 == 0:
		saida.write("<div style='clear:both'></div>")
	i+=1

#fechamento do arquivo
saida.close()