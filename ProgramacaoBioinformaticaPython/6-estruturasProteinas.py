#módulo que permite a manipulação de estruturas de proteinas salvas em PDB
from Bio.PDB import *

'''
Bio.PDB trabalha:
1-> lendo o arquivo tridimencional de uma proteina
2-> converte em um objeto do tipo instructor
3-> analisa um determinada Hierarquia/Arquitetura (Hierarquia SMCRA)
	->apartir da leitura da estrutura de uma proteina, ela converte 
	em várias camadas que permitem a navegação entre elas
'''

#
parser = PDBParser()

#leitura de um arquivo
estrutura = parser.get_structure("1BGA", "1bga.pdb")

""" 
NAVEGANDO PELA HIERARQUIA RMCRA 
-> parte por parte da arquitetura
"""
#pegando 1 dos modelos da proteina
modelo = estrutura[0]
#pegando uma das cadeias da modelo[0]
cadeia_A = modelo["A"]
#pegando um dos resíduos da cadeia_A
resido_100 = cadeia_A[100]
#pegando o Carbono Alfa do residuo_100
carbono_Alfa = resido_100['CA']

'''
REALIZANDO ALGUMAS ANÁLISES
'''

#Para o calculo de distância euclidiana entre 2 atomos
atamo_100 = estrutura[0]['A'][100]['CA']
atamo_101 = estrutura[0]['A'][101]['CA']
#a ação realizada acima é o mesmo feitas pelas variaveis, porém, de forma direta

#DISTANCIA EUCLIDIANA
distancia = atamo_101 - atamo_100
print(distancia)