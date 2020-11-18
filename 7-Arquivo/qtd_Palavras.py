arq = open("texto.txt", "r")
texto = arq.read()
arq.close()

vet_palavras = []
vet_qtd = []
texto = texto.split()
for palavra in texto:
    flag = 0
    tam = len(vet_palavras)
    cont = 0
    while cont < tam:
        if vet_palavras[cont] == palavra:
            vet_qtd[cont] += 1
            flag = 1
        cont += 1
    if flag == 0:
        vet_palavras.append(palavra)
        vet_qtd.append(1)

for i in range(len(vet_palavras)):
    print("a palavra '{0}' se repete {1} vezes".format(vet_palavras[i], vet_qtd[i]))