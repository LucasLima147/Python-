# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:50:14 2020

@author: lucas
"""
import os

texto = "Cientista de dados é a profissão que mais tem crecido em todo mundo.\n"
texto += "Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning.\n"
texto += "E claro Big Data."

#se um arquivo for aberto em modo escrita e não existir, o Python irá crialo
'''arq1 = open(os.path.join('arqs/cientista.txt'), 'w')
for word in texto.split():
    arq1.write(word + " ")
arq1.close()
arq1 = open("arqs/cientista.txt", 'r')
print(arq1.read())
print("\n\n")'''
#############################################################################
'''     TRABALHANDO COM ARQUIVOS CSV        
import csv                                                      # importando o pacote csv     

# escrevendo dados no arquivo
with open('arqs/numeros.csv', 'w') as arquivo:
    writer = csv.writer(arquivo)                                # metodo para poder começar a gravar dados
    writer.writerow(("primeira", "segunda", "terceira"))        # gravando os daods nos arquivos
    writer.writerow((55, 93, 76))
    writer.writerow((62, 14, 86))

# lendo os dados do aquivo
with open('arqs/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)                                # metodo para ler os dados do arquivo 
    for col in leitor:                                          # pegando cada linha do arquivo
        print("Numero da coluna", len(col))                     # imprimindo o número de colunas
        print(col)                                              # imprimindo os dados

# transformando os dados em uma lista
with open('arqs/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)                                        # convertendo os dados em uma lista
for row in dados[1:]:                                           # percorrendo os dados a partir da primeira linha
    print(row)                                                  # imprimindo cada linhda'''

#############################################################################
'''     TRABALHANDO COM ARQUIVOS JSON       '''
import json
with open("arqs/dados.json", "r") as arquivo:                   # abrindo um arquivo Json
    texto = arquivo.read()                                      # lendo o conteúdo
    dados = json.loads(texto)                                   # carregando os dados do json (dicionário)
print(type(dados))
print(type(texto))

"""     imprimindo um Json da internet       """
# importando pacote para download de arquivos
from urllib.request import urlopen
# buscando o arquivo e lendo o conteúdo do json no formato utf8
response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
# carregando o arquvio json para o objeto data
data = json.loads(response)[0]
print("Titulo:", data['title'])
print("URL:", data['url'])
print("Duração do vídeo:", data['duration'])
print("Numero de visualizações:", data['stats_number_of_plays'])

"""     copiando o conteúdo de um arquivo para outro        """
import os                                                   # importando pacote para usar funções do S.O
arq_fonte = "arqs/dados.json"
arq_destino = "arqs/json_data.txt"

# Método 1
with open(arq_fonte, "r") as infile:                        # abrindo o arquivo Json
    conteudo = infile.read()                                # lendo o conteúdo na variável
    with open(arq_destino, "w") as outfile:                 # abrindo o arquivo txt
        outfile.write(conteudo)                             # carregando o conteúdo no arquivo
    print("o conteúdo carregado foi:\n", conteudo)

# Méodo 2 -> fazendo tudo direto
open(arq_destino, 'w').write(open(arq_fonte, 'r').read())

# imprimindo o conteúdo final do arquivo de destino
with open(arq_destino, 'r') as arquivo:
    data = json.loads(arquivo.read())                      # carregando o conteúdo do arquivo e convertendo em Json
    print(data)