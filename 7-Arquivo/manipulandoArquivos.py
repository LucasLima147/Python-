arq1 = open("arqs/arquivo1.txt", "r")						# abrindo um arquivo para leitura
print(arq1.read())											# Apenas lendo o conteúdo / o restante do conteúdo
print(arq1.tell())											# conta a quantidade de caracter
print(arq1.seek(0,0))										# retorna em um ponto específico do arquivo (linha, coluna)
print(arq1.read(10))										# posso passar a quantidade de caracter que desejo ler

arq2 = open("arqs/arquivo1.txt", "w")						# abrindo o arquivo para escrita
arq2.write("testando gravacao de arquivos em Python")		# sobrescrevendo o arquivo (perde tudo que já estava nele)
arq2.close()												# fechando o arquivo

arq3 = open("arqs/arquivo1.txt", "a")						# abrindo o arquivo como append (Acrescentar)
arq3.write("\nacressentando conteúdo")  					# acrescentando conteúdo ao arquivo
arq3.close()                                                 

arq4 = open("arqs/teste.txt", "r")                          # abrindo o arquivo novo
print(arq4.read())                                          # lendo o arquivo todo
arq4.seek(0)                                                # voltando ao início do arquivo
rows = arq4.readlines()                                     # salvando as linhas do arquivo comos lista
print(rows)                                                 # printando a lista gerada
arq4.close()

for row in open("arqs/teste.txt", "r"):                     # podemos ainda ler cada linha com o for
    print(row)                                              # OBS: se quiser tirar o "\n", use o strip()

##################################################################################
'''     CRIANDO ARQUIVOS COM O USUÁRIO      '''
fileName = input("digite o nome do arquivo: ")              # user digitando o nome do arquivo
fileName += ".txt"                                          # colocando a extenção do arquivo

f = open(fileName, "w")                                     # criando o arquivo .txt
f.write("incluindo texto no arquivo criado")                # escrevendo no arquivo
f.close()                                                   # fechando o arquivo

##################################################################################
'''     USO DO TERMO with PARA MANIPULAÇÃO DE ARQUIVOS      '''
#OBS: geralmente usado para comandos rápidos 
with open('arqs/cientista.txt', 'r') as arquivo:            # with faz o .close() automáticamente
        conteudo = arquivo.read()
print(conteudo)

