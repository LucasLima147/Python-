f = open("arqs/salarios.csv", "r")          # abrindo arquivo .csv
data = f.read()                             # lendo e salvando o conteúdo do arquivo na variável
rows = data.split("\n")                     # transformando cada linha em uma lista
full_data = []                              
for row in rows:                            # for para ler cada linha
    split_row = row.split(",")              # transformando cada coluna em uma lista local
    full_data.append(split_row)             # salvando as colunas em uma lista externa

first_row = full_data[0]                    # salvando a primeira coluna na variável
print(len(full_data), len(first_row))       # mostando a quantidade de linhas e colunas'''

#################################################################################
     MANIPULANDO DADOS COM O PANDAS      
# pandas é um dos mais usados para manipular diversos tipos de arquivos
import pandas as pd                         # importando o pacote pandas

file_name = "arqs/binary.csv"               # escrevendo o caminho do arquivo
df = pd.read_csv(file_name)                 # abrindo o arquivo em leitura para csv
print(df.head())                            # mostrando o arquivo .cvs formatado com Pandas
file2 = "arqs/salarios.csv"
df2 = pd.read_csv(file2)
print(df2.head())

#################################################################################
'''     MANIPULANDO DADOS COM JSON      '''
#json nada mais é do que um dicionário em Python mas em uma string
dicionario = {'nome': 'Lucas Lima',
              'linguagem': "python",
              'similar': ['c', 'Modula-3', 'lisp'],
              'users': 1000000}

import json                                 # importando o pacote json
print(type(dicionario))                     # aqui ainda como dicionário
arq = json.dumps(dicionario)                # convertendo para Json
print(type(arq))                            # arquivo já no formato Json