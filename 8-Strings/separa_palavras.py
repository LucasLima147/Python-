texto = input("Digite o texto: ")

# texto += " "
vet = []
tam = len(texto)
inicio = 0
cont = 0
while (cont < tam):
    if texto[cont] == " ":
        vet.append(texto[inicio:cont])
        inicio = cont+1
    if cont+1 == tam:
        vet.append(texto[inicio:cont+1])
    cont += 1

print(vet)