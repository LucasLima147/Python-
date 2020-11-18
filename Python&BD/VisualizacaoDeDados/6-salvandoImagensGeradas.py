# Visualização de dados em Python
import matplotlib.pyplot as plt
 
x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 3300, 100]
 
titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"
 
# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)
 
plt.plot(x, y, color="#000000", linestyle="--")
plt.scatter(x, y, label="Meus pontos", color="k", marker=".", s=z)
plt.legend()
plt.show()

'''
.savefig() -> para salvar a figura do gráfico
	-> os argumentos são ("NomeFigura.extenção", dpi='tamnho/resolução')
'''
#gerando só uma figura
plt.savefig("figura1.png")
#gerando um pdf
plt.savefig("figura1.pdf")
#figura com tamanho de 32
plt.savefig("figura1.pdf", dpi=32)
#tamnho melhor, mais genérico(recomendado)
plt.savefig("figura1.pdf", dpi=32)
#tamanho pedido, as vezes, por algumas revistas
plt.savefig("figura1.pdf", dpi=1200)