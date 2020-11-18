N = int(input("Digite o numero de alunos: "))
# provas
prova1 = [0] * N
prova2 = [0] * N
'''Resolução principal'''
#leitura da prova 1
cont = 0
media1 = 0.0
while cont < N:
    prova1[cont] = float(input("Digite o valor da nota do aluno da prova 1: "))
    prova2[cont] = float(input("Digite o valor da nota do aluno da prova 2: "))
    cont += 1
##########
cont = 0
while cont < N:
    print((prova1[cont] + prova2[cont])/2)
    cont += 1