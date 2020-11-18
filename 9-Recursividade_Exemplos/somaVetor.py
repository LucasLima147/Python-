# funcao
def somaVetor(vet, N):
	if N == 0:
		aux = vet[N]
	else:
		aux = vet[N] + somaVetor(vet, N-1)

	return aux

# MAIN
vet = [1, 4, 3, 6, 1]
N = len(vet) - 1
resp = somaVetor(vet, N)
print(resp)