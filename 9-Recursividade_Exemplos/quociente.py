def quociente(numero, divisor):
	if numero < divisor:
		aux = 0
	else:
		aux = 1 + quociente((numero-divisor), divisor)

	return aux

numero = 10
divisor = 2
resp = quociente(numero, divisor)
print(resp)