Maior = int(input("Digite um número: "))
Menor = 0
cont = 1

while cont <= 19:
    teste = int(input("Digite outro número: "))
    if teste > Maior:
        maior = teste
    elif teste > Menor:
    	Menor = teste
    cont = cont + 1

print("O maior foi: ", Maior, ", e o menor foi: ", Menor)