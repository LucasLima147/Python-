#Boxplot - Diagrama de caixa
import matplotlib.pyplot as plt
import random

#vetor vazio
vetor = []
#gerando os numeros aleatórios
for i in range(100):
	vetor.append(random.randint(0,50))

#gerando o gráfico de caixa
plt.boxplot(vetor)
plt.title("Diagrama de caixas -> Boxplot")
plt.show()
