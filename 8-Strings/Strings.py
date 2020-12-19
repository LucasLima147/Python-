"""algumas funções possíveis com strings"""
A = "lucas "
B = "LIMA"
############################
""" concatenar (+) strings """
juntar = A + B 
print(juntar, "\n")

""" len() -> numero de instens no (objeto) """
tamanho = len(R)
print(tamanho, "\n")

""" exebir posição de um caracter da string """
#funciona tipo como um vetor
print(A[0], B[2]) 
print(juntar[0:5], "\n") # : significa até

""" lower() -> passar tudo pra caixa baixa """
""" upper() -> passar tudo pra caixa alta """
A = A.upper()
B = B.lower()
print(A, B)
# posso simplesmente usar dentro do print sem alterar minha variável

""" strip() -> remove caracteres especiais NO COMEÇO e NO FIM"""
C = "\nLucas "
print(len(C), C.strip(), len(C.strip()))

""" split() -> converte em uma lista """
# é realizado pelo caracter " " (espaço)
D = A + B
print(D.split())
#pode-se fazer a separação de outras
#isso é feito passando parâmetros a função
E = "O rato roeu a roupa do rei de roma"
print(E.split("r"), "\n")

" find() -> encontrar letra/ termo em uma string"
print(E.find("rei"))
#exemplo de utilidade
busca = E.find("rei")
print(E[busca: ], "\n")
# se a função find() não encontrar o paramentro, ele retora -1

""" replace() -> busca um valor e troca por outro """
#só funciona trocando valores do tipo STRING
F = E.replace("o rei", "a rainha") # o que vou trocar, valor a ser trocado
print(F)
print(E.replace("O rato", "A ratasana"), "\n")