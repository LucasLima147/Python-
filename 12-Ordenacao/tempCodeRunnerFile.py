def selection_sort(vetor):
    inicio = time.time()
    for i in range(len(vetor)-1):
        menor = min(vetor)
        for j in range(i+1, len(vetor)):
            if vetor[j] < vetor[menor]:
                menor = j

        aux = vetor[i]
        vetor[i] = vetor[menor]
        vetor[menor] = aux
    fim = time.time()
    print("Selection Sort concluido")
    listar_vetor_primeiros(vetor)
    listar_vetor_ultimos(vetor)
    return int(fim - inicio)