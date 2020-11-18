def elevacao(base, potencia):
	if potencia == 0:
		aux = 1
	else:
		aux = base * elevacao(base, potencia-1)

	return aux

base = 11
potencia = 50
resp = elevacao(base, potencia)
print(resp)