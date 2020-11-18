import gmodulos

Vertices = 7 # Quantidade de vértices (Nós). 

Grafo = [[0]*Vertices for i in range(Vertices)] # Cria o Grafo (matriz) Vertices x Vertices 

# Cada par é uma Tupla (Um tipo de estrutura de dados do Python)
# A vaiável Arestas é uma lista de tuplas
Arestas = [(0, 1), (1, 0), (0, 2), (2, 0), (0, 3), (3, 0), (1, 4), (4, 1), (3, 4), (4, 3), (4, 5), (5, 4), (4, 6), (6, 4), (5, 6), (6, 5)]

gmodulos.cria_matriz(Grafo, Vertices, Arestas)

gmodulos.imprime_matriz(Grafo, Vertices)

NO = 1
gmodulos.amplitude(Grafo, Vertices, NO-1)
print()
gmodulos.profundidade(Grafo, Vertices, NO-1)