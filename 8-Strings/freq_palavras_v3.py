from collections import Counter

frase = input("Digite um texto: ").split()
c = Counter(frase)
print(c)