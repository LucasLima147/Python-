'''
Gráfico de Disperção/de pontos
em python: Scatterplot
'''

#importar a bíblioteca gráfica Matplotlib.Pyplot
import matplotlib.pyplot as plt


#título, descrições e legendas para o gráfico
titulo = "Gráfico de Disperção/de Pontos"
descEixoX = "Eixo X"
descEixoY = "Eixo Y"
lengenda1 = "Icebom"
lengenda2 = "FAI-MG"

#título
plt.title(titulo)

#descrições do eixo X e Y (LABELs)
plt.xlabel(descEixoX)
plt.ylabel(descEixoY)

'''
GERANDO UM GRÁFICO
->plt.bar(x, y) 
	-> X e Y são, cada um, uma lista de coordenadas em cada eixo
'''

#eixo X deve ser linear
x1 = [1, 3, 5, 7, 9]
x2 = [2, 4, 6, 8, 10]
#altura de cada coluna
y1 = [5, 8, 3, 4, 5]
y2 = [6, 2, 4, 3, 1]

'''
Neste caso, usaremos dois métodos:
-> .scatter() para gerar os pontos
-> .plot() para gerar as linhas que ligam os pontos
'''
#pontos da legenda 1
plt.scatter(x1, y1, label = lengenda1)
plt.plot(x1, y1)
#ponto da legenda 2
plt.scatter(x2, y2, label = lengenda2)
plt.plot(x2, y2)

#plt.legend() é para mostrar as legendas
plt.legend()

#plt.show() -> mostra tudo o que foi gerado para o gráfico
plt.show()