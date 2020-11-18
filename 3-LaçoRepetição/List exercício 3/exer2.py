print("Quando quiser parar, digite -1. VAMOR COMEÇAR !!!!!")
maior = int(input("Digite um número inicial: "))
pare = 0 

while pare != -1:
    teste = int(input("Digite um número qualquer: "))
    if teste > maior:
        maior = teste
    else:
        Menor = teste
    pare = teste

print("O maior foi: ", maior, ", e o menor foi: ", Menor)