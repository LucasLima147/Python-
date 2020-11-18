#importando os módulos/arquivos com as funções.
import aleatorio as a #apelidando aleatorio como a
import medias as m #apelidando media como m

lista = a.criaraleatorio(10)
print("essa é a minha lista \n", lista, "\n")

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)
print(lista)
print("A média dos valores é:", media)
print("A mediana é:", mediana)
print("A moda é:", moda)