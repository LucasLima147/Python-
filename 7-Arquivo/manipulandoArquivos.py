arq1 = open("arqs/arquivo1.txt", "r")						# abrindo um arquivo para leitura
print(arq1.read())											# Apenas lendo o conteúdo / o restante do conteúdo
print(arq1.tell())											# conta a quantidade de caracter
# retorna em um ponto específico do arquivo (linha, coluna)
print(arq1.seek(0, 0))
# posso passar a quantidade de caracter que desejo ler
print(arq1.read(10))

arq2 = open("arqs/arquivo1.txt", "w")						# abrindo o arquivo para escrita
# sobrescrevendo o arquivo (perde tudo que já estava nele)
arq2.write("testando gravacao de arquivos em Python")
arq2.close()												# fechando o arquivo

# abrindo o arquivo como append (Acrescentar)
arq3 = open("arqs/arquivo1.txt", "a")
# acrescentando conteúdo ao arquivo
arq3.write("\nacressentando conteúdo")
arq3.close()

# abrindo o arquivo novo
arq4 = open("arqs/teste.txt", "r")
# lendo o arquivo todo
print(arq4.read())
# voltando ao início do arquivo
arq4.seek(0)
# salvando as linhas do arquivo comos lista
rows = arq4.readlines()
# printando a lista gerada
print(rows)
arq4.close()

# podemos ainda ler cada linha com o for
for row in open("arqs/teste.txt", "r"):
    # OBS: se quiser tirar o "\n", use o strip()
    print(row)

##################################################################################
# '''     CRIANDO ARQUIVOS COM O USUÁRIO      '''
# fileName = input(
#     "digite o nome do arquivo: ")              # user digitando o nome do arquivo
# # colocando a extenção do arquivo
# fileName += ".txt"

# # criando o arquivo .txt
# f = open(fileName, "w")
# # escrevendo no arquivo
# f.write("incluindo texto no arquivo criado")
# f.close()                                                   # fechando o arquivo

##################################################################################
'''     USO DO TERMO with PARA MANIPULAÇÃO DE ARQUIVOS      '''
# OBS: geralmente usado para comandos rápidos
with open('texto.txt', 'r') as arquivo:            # with faz o .close() automáticamente
    conteudo = arquivo.read()
print(conteudo)
