'''
Vamos usar os métodos CAll() e CHECK_OUTPUT()
Para isso importaremos o módulo 'subprocess'
	> permite a manupacao de saída de outros programas
'''
import subprocess

'''
O método .call() funciona APENAS PARA EXECUTAR comandos
->cada parametro dentro dele é uma parte do comando em uma lista
	>subprocess.call([parte1, parte2, ... , parte_final])
'''
print("PARTE 1")
subprocess.call(["python", "scriptDosExemplos.py"])

'''
***** MANIPULANDO A SAÍDA DE UM PROGRAMA *****
para MANIPULAR a saída de um progama utilizamos o método check_output()
->check_output() funciona como o  método call()
	>cada parametro é um comando, passados dentro de uma lista
->a diferença está na possibilidade de armazenar a saída em uma variavel
	>com isso,´podemos manipular essa saída a nossa vontade
'''

print("\n\nPARTE 2")
saida = subprocess.check_output(["python", "scriptDosExemplos.py"])
print(f"forma que já vem do comando: {saida}")

#a forma que eu quero
saida = str(saida.strip()) #retira os caracteres especiais
saida = saida.replace(saida[0:1], "") #retirando o 'b'
print(f"Saída no momento: {saida}") #com as aspas simples
saida = saida.replace("'", "")
print(f"A saída que eu quero: {saida}") #sem as aspas simples