def cria_matriz(Grafo, Vertices, Arestas):  
    # cada tupla
    for Aresta in Arestas:
        # Grafo[linha][coluna] = 1
        Grafo[Aresta[0]][Aresta[1]] = 1

def imprime_matriz(Grafo, Vertices):
    # cada tupla 
    for i in range(Vertices):
        # end="" não pula linha
        print(" ", i+1, end="")
    for lin in range(Vertices):
        print()
        print(lin+1, end=" ")
        for col in range(Vertices):
            print(f"{Grafo[lin][col]}", end="  ")
    print()

# apenas a olha o valor do nó acessado 
def visita(N):
    print(N+1, end=",")

def enfileire(N, F):
    F.append(N)

def desenfileire(F):
    N = F.pop(0)
    return N

# amplitude(grafo pronto, num_vertices, nó_inicial)
def amplitude(Grafo, Vertices, N):
    # sinaliza quando ele foi marcado
    Marca = [0]*Vertices # Inicializa o vetor Marca com zeros
    F = [] # Inicializa a Fila vazia. A Fila está sendo criada em uma lista de Python
    visita(N)
    # sinaliza qual posição já foi visitada
    Marca[N] = 1
    # coloca o valor visitado na fila
    enfileire(N, F)

    while len(F) != 0:
        # tira o valor do fila
        T = desenfileire(F)
        W = 0
        while W < Vertices:
            # Verifica no grafo se é 1 (visinho) .E. se j[a foi marcado]
            if Grafo[T][W] == 1 and Marca[W] == 0:
                # mostra na tela
                visita(W)
                # sinaliza a lista de marcados
                Marca[W] = 1
                # coloca o que já foi visitado na lista
                enfileire(W, F)
            W += 1
# ============================================

""" Modulos de PROFUNDIDADE """
def empilhar(P, N):
    P.append(N)

def desempilhar(P):
    N = P.pop()
    return N

def profundidade(Grafo, Vertices, N):
    Marca = [0]*Vertices
    Pilha = []
    visita(N)
    Marca[N] = 1
    empilhar(Pilha, N)
    topo = len(Pilha)
    while topo > 0:
        T = desempilhar(Pilha)
        topo -=1
        W = 0
        while W < Vertices:
            if Grafo[T][W] == 1 and Marca[W] == 0:
                visita(W)
                Marca[W] = 1
                empilhar(Pilha, T)
                topo += 1
                T = W
                W = 0
            else:
                W += 1

    