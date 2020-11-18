Cadeia = input("Cadeia: ")
Palavras_separadas = Cadeia.split()                     # Cria uma lista com as palavras da cadeia
Dicionario = {}                                         # Incializa um dicionário vazio

for Palavra in Palavras_separadas:                      # Em cada iteração a variável Palavra recebe uma chave do dicionário
    if Palavra in Dicionario:                           # Verifica se uma determina chave (variável Palavra) já existe no dicionário
        Dicionario[Palavra] = Dicionario[Palavra] + 1   # Se a chave já existe, conta mais um no valor corresponde a chave
    else:
        Dicionario[Palavra] = 1                         # Se a chave não existe, um novo item é adicionado ao dicionário com a nova palavra e o valor = 1

for Palavra in Dicionario:                              # Em cada iteração é escrito a palavra e sua correspondente frequência na cadeia
    print(Palavra, Dicionario[Palavra])