''' 
Caso não saiba os módulos do pacorte ou o que faz/retorno de cada módulo, use:
   print(dir(pacote)) -> listar todos os módulos do pacote
   help(pacote) -> lista os módulos e seus retornos
   help(pacote.modulo(parametro_se_tiver)) -> mostra o retorno específico do módulo e outras informações                           

Caso queira importar somente o módulo específico do pacote:
   from pacote import modulo -> forma de importar o módulo específico
   modulo() ou modulo.função() -> como usar no código
'''

# ----------- Pacote MATH: para calculos matemátivos -----------
import math
#from math import sqrt 
print(math.sqrt(100))                           # .sqrt(número) -> raiz quadrada
print('.............................. \n')

# ----------- Pacote RANDOM: valores aleatórios -----------
import random
#from random import randint
print(random.choice([0, 100, 2546, 8567]))       # .choice(lista) -> valor aleatório da lista de parâmetro
print(random.sample(range(100), 10))            # .sample(range de número, quantidade) -> amostra de números
print(random.randint(0, 200))                   # .randint(de, até) -> um valor inteiro dentro dos limites passados
print('.............................. \n')

# ----------- Pacote STATISTICS: operações estatísticas -----------
dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
import statistics
#from statistics import median
print(statistics.mean(dados))                   # .main(lista) -> retorna a média
print(statistics.median(dados))                 # .median(lista) -> retorna a mediana
print('.............................. \n')

# ----------- Pacote OS e SYS: operações do Sistema Operacional -----------
import os
#from os import system
print(os.getcwd())                              # .getcwd() -> mostra o diretório atual
os.system("pause")                              # .system("comando") -> executar comandos como se fosse no terminal

import sys
sys.stdout.write("teste \n 01")                 # .stdout.write("texto") -> escrever algo na tela do terminal
print('.............................. \n')

# ----------- Pacote URLLIB.REQUEST: buscar url -----------
import urllib.request

# carrega o objeto criado pela coneção com a url do parâmetro
reposta = urllib.request.urlopen("https://www.python.org/")
print(reposta)

# carregando o conteudo do código html para a variável
html = reposta.read()
print(html)