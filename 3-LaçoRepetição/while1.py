maior = int(input("Digite um primeiro número"))
cont = 1

# Laco de repeticao
while cont <= 99:
    numero = int(input("digite o segundo número para comparação"))
    if maior < numero:
        maior = numero
    cont = cont + 1

print(maior)
