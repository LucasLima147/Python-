def somaValores(N):
	if N == 0:
		aux = 0
	else:
		aux = N + somaValores(N - 1)

	return aux

print(somaValores(500))