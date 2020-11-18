#importar a bíblioteca gráfica Matplotlib.Pyplot
import matplotlib.pyplot as plt


#gerando um título para o gráfico
plt.title("Gráfico de Linhas")

#descrições do eixo X e Y (LABELs)
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

'''
GERANDO UM GRÁFICO
->plt.plot(x, y) 
	-> X e Y são, cada um, uma lista de coordenadas em cada eixo
'''

x = [1, 3, 5]
y = [2, 4, 6]
#gerando o gráfico de linhas -> .plot()
plt.plot(x, y)

#plt.show() -> mostra tudo o que foi gerado para o gráfico
plt.show()