# MODULOS
def cria_matriz(Grafo, Vertices, Arestas):  
    # cada tupla
    for Aresta in Arestas:
        # Grafo[linha][coluna] = 1
        Grafo[Aresta["aresta"][0]][Aresta["aresta"][1]] = Aresta["km"]

def imprime_KM(Grafo, Num_cidades):
	print("   Origem     Destino     Distância")
	Origem = 0
	while Origem < Num_cidades:
		Destino = 0
		Destino_menor = 0
		menor_distancia = 0
		while Destino < Num_cidades:
			if Grafo[Origem][Destino] != 0:
				distancia = Grafo[Origem][Destino]
				if distancia < menor_distancia or menor_distancia == 0:
					menor_distancia = distancia
					Destino_menor = Destino
			Destino += 1

		print("     "+str(Origem+1)+"          "+str(Destino_menor+1)+"          "+str(menor_distancia)+" Km")
		Origem += 1
# MAIN
Vertices = 7

Grafo = [[0]*Vertices for i in range(Vertices)]

Arestas = [{"aresta":(0, 1), "km": 25}, {"aresta":(1, 0), "km": 25},
{"aresta":(0, 2), "km": 10}, {"aresta":(2, 0), "km": 10},
{"aresta":(0, 3), "km": 20}, {"aresta":(3, 0), "km": 20},
{"aresta":(1, 4), "km": 50}, {"aresta":(4, 1), "km": 50},
{"aresta":(3, 4), "km": 23}, {"aresta":(4, 3), "km": 23},
{"aresta":(4, 5), "km": 8}, {"aresta":(5, 4), "km": 8},
{"aresta":(4, 6), "km": 12}, {"aresta":(6, 4), "km": 12},
{"aresta":(5, 6), "km": 5}, {"aresta":(6, 5), "km": 5}]

cria_matriz(Grafo, Vertices, Arestas)
imprime_KM(Grafo, Vertices)