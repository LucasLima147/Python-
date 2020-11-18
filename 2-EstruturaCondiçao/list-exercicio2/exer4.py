Sexo = input("Digite: \n M - Mulhuer; \n H - Homem \n Escolha: ")
Altura = float(input("Digite sua altura: "))

if Sexo == "M":
    PesoI = (62.1 * Altura) - 44.7
    print("Seu peso ideal é: ", PesoI)
elif Sexo == "H":
    PesoI = (72.7 * Altura) - 58
    print("Seu peso ideal é: ", PesoI)
else:
    print("Letra do sexo inválida ou digitou em minisculo")