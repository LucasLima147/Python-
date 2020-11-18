N = int(input("numero de alunos: "))
notas = [0] * N

cont = 0
while cont < N:
    notas[cont] = float(input("Digite a nota do aluno: "))
    cont += 1

media = 0.0
cont = 0
while cont < N:
    media = media + notas[cont]
    cont += 1
media = media / N

cont = 0
aprovado = 0
reprovados = 0 
while cont < N:
    if notas[cont] >= 7:
        aprovado += 1
    else:
        reprovados += 1
    cont += 1
print(media, aprovado, reprovados)