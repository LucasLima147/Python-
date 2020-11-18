#módulo do python para acessar as funções do SO (shell)
import os

'''
método sistem("comando")
->permite executar comando do terminal
	>o exemplo abaixo está mostrando como printar algo na tela
	>echo (terminal) == print() (python3)

além disso, posso usar outros comandos do shell terminal
'''
os.system("echo hellow Word")

'''
EXEMPLO 1: LIMPEZA DE TELA
usaremos a função input() para pegar algo digitado pelo usuário
---> caso ele digite 's', iremos limpar a tela,
---> caso ele digite 'n', iremos exibir a mensagem "voce nao limpou a tela"
---. caso digite outra coisa, aparecerá 'comando invalido'
'''
#pegando o que o usuario digitar
var = input("Deseja limapr a tela? (s/n)")
if var == 's':
	os.system("cls")
	os.system("echo A tela foi limpada com sucesso")
elif var == 'n':
	os.system("voce nao quis limpar a tela")
else:
	os.system("opcao invalida")



"""
EXEMPLO 2: SCRIPT EXECUTANDO OUTRO SCRIPT
"""
print("\n\n")
print("TESTE 2")
variavel = os.system("python scriptDosExemplos.py > output.txt")
arquivo = open("output.txt").read()
print("A mensagem executada foi: ", arquivo)