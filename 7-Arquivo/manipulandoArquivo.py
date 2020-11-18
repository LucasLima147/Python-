""" open() -> função para abrir um arquivo """
''' var = open(nome, modo) onde: 
 -> NOME = nome do arquivo/pasta;
 -> MODO = forma que abriremos o arquivo, sendo esses modos:
 	-> r: somente leitura
 	-> w: escrita (se existir será apagado e será criado um novo)
 	-> a: leitura e escrita (conteúdo no final)
 	-> r+: leitura e escrita
 	-> w+: escrita (mesma coisa do w)
 	-> a+: leitura e escrita (atualização do arquivo) '''

"""lendo um arqivo"""
teste = open("arquivo.txt")
#metodo readlines() -> lê o arquivo e armazena em uma lista
linhas = teste.readlines()
print(linhas, "\n")

"""criando um arquvio """
w = open("criado.txt", "a")
w.write("esse eh o meu arquivo\n")
w.close()
leitura = open("criado.txt")
leitura = leitura.readlines()
print(leitura)