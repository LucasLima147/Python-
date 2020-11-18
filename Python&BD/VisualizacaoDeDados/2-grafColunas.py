#importar a bíblioteca gráfica Matplotlib.Pyplot
import matplotlib.pyplot as plt


#gerando um título para o gráfico
plt.title("Grpafico de Colunas")

#descrições do eixo X e Y (LABELs)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

'''
GERANDO UM GRÁFICO
->plt.plot(x, y) 
	-> X e Y são, cada um, uma lista de coordenadas em cada eixo
'''

#eixo X deve ser linear
x = [1, 3, 5]
#altura de cada coluna
y = [2, 4, 6]

#gerando o gráfico de colunas -> .bar()
plt.bar(x, y)

#plt.show() -> mostra tudo o que foi gerado para o gráfico
plt.show()