N = int(input("Digite o número de alunos: "))
notas = [0]*N
cont = 0
media = 0

while cont < N:
    notas[cont] = float(input("Digite a nota do aluno: "))
    media += notas[cont]
    cont += 1
media /= N

perAcima = 0
perAbaixo = 0
for nota in notas:
    if nota >= media:
        perAcima += 1
    else:
        perAbaixo += 1

perAcima = (perAcima/N) * 100
perAbaixo = (perAbaixo/N) * 100

print("A porcentagem de alunos acima da média é de {0:.2f}% e a menor é {1:.2f}%".format(perAcima, perAbaixo))       