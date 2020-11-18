Num = int(input("Digite um Numero: "))

fatorial = 1
while Num >= 1:
    fatorial = fatorial * Num
    Num = Num - 1

print("O seu fatorial é: ", fatorial)