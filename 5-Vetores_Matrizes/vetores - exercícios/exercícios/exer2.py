N = int(input("Digite o numero de valores inteiros: "))
vetor = [0] * N
cont = 0
while cont < N:
    vetor[cont] = int(input("Digite um valor: "))
    cont += 1

cont = 0
par = 0
imper = 0
while cont < N:
    if (vetor[cont] % 2) == 0:
        par += 1
    else:
        imper += 1
    cont += 1

print(par, imper)