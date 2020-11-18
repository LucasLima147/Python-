"""vetores que serão usados"""
valor1 = [0] * 20
valor2 = [0] * 20 
operac = [0] * 20
result = [0] * 20
#============================
cont = 0
while cont < 20:
    valor1[cont] = int(input("VETOR 1: "))
    valor2[cont] = int(input("VETOR 2: "))
    operac[cont] = input("Digite um dos operadores basicos: ")
    cont += 1
#--------------------------
cont = 0
while cont < 20:
    if operac[cont] == "+":
        result[cont] = valor1[cont] + valor2[cont]
    elif operac[cont] == '-':
        result[cont] = valor1[cont] - valor2[cont]
    elif operac[cont] == '*':
        result[cont] = valor1[cont] * valor2[cont]
    elif operac[cont] == '/':
        result[cont] = valor1[cont] / valor2[cont]
    print("valores:", valor1[cont], valor2[cont], " | operação: ", operac[cont], " | resultado: ", result[cont])
    cont += 1