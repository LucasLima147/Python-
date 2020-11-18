'''
DICIONARIOS => Nada mais é do que um vetor, porém, em vez de [ ], usamos { }
->A diferença se dá por você passar uma identificação para determinado valor
	-> tipo uma chave
'''
# Meu Dicionairo
dicionario = {'nome': "Lucas Lima", 'idade': 18, 'curso': "introducao a Python"}

#mostrando o dicionario inteiro...
print(dicionario)
#... o valor da chave nome...
print(dicionario['nome'])
#... o valor da chave idade...
print(dicionario['idade'])
#... o valor da chave curso...
print(dicionario['curso'], "\n \n")

# podemos mostrar usando o FOR 
for chave in dicionario:
	#para mostrar quais são as chaves
	print(chave)
	#para mostrar o valor da chave
	print(dicionario[chave], "\n")

print("\n \n")
# pode-se também passar os valores no FOR como uma tupla
# isso é feito com o metodo items()
for i,j in dicionario.items():
		print(i,j)
""" existem outras duas formas de navergar pelo meu DICIONARIO
->pelos valores:
	->substituo o .items() por .values()
->pelas chaves:
	->substiuto o .items() por keys()
"""

#podemos ainda fazer uma concatenação de dois dicionários
#metodo update(dicionario)
dicionario2 = {"lucas": "Erika", "lima":"Martins"}
dicionario.update(dicionario2)
print(dicionario)
# Isso irá atualizar os dois dicionários