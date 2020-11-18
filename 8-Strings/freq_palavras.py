def palavras_texto(texto):
    texto = texto.split()
    palavras = []

    for word in texto:
        flag = 0
        cont = 0
        qtd = len(palavras)
        while cont < qtd:
            if palavras[cont] == word:
                flag = 1
            cont += 1
        if flag == 0:
            palavras.append(word)
    
    return palavras

def contagem_palavras(words, texto):
    for word in words:
        qtd_palavra = texto.count(word)
        print("a palavra '{0}' se repete {1}".format(word, qtd_palavra))

##########################################
frase = input("Digite um texto: ")

words = palavras_texto(frase)
contagem_palavras(words, frase)

