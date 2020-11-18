Cadeia = input("Cadeia: ")
Palavras_separadas = Cadeia.split()                         # Cria uma lista com as palavras da cadeia
Palavras = []                                               # Inicializa a lista Palavras
Frequencias = []                                            # Inicializa a lista Frequencias

for Word in Palavras_separadas:                             # A variável Word recebe cada palavra da lista Palavras_separadas
    try:
        indice = Palavras.index(Word)                       # Procura a palavra (Word) na lista Palavras e retorna o seu índice
    except:
        Palavras.append(Word)                               # Se a palavra (Word) não for encontrada, ela será acrescentada na lista Palavras
        Frequencias.append(1)                               # e também será inserido o valor 1 na lista Frequencias
    else:
        Frequencias[indice] += 1                            # Se a palavra (Word) for encontrada será computado mais 1 a lista Frequencias

for indice, Word in enumerate(Palavras):                    # As variávesi indice e Word receberão respsctivamente o valor do índice e a
    print(indice, Word, " - ", Frequencias[indice])         # palavra correspondente da lista Palavras