def palavras_texto(texto):
    texto = texto.split()
    palavras = []
    contador = []

    for word in texto:
        flag = 0
        cont = 0
        qtd = len(palavras)
        while cont < qtd:
            if palavras[cont] == word:
                flag = 1
                contador[cont] += 1
            cont += 1
        if flag == 0:
            palavras.append(word)
            contador.append(1)
    
    for cont in range(len(palavras)):
        #print("A palavra '{0}' aparece {1} vezes".format(palavras[cont], contador[cont]))
        print("A palavra %s aparece %i vezes" %(palavras[cont], contador[cont]))

##########################################
frase = "meu nome eh lucas lucas lima meu eh eh eh eh eh lucas"
palavras_texto(frase)