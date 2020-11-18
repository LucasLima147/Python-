def resto(numero, divisor):
	if divisor > numero:
		aux = numero
	else:
		aux = resto(numero-divisor, divisor)

	return aux

# MAIN
num = int(input("Digite um valor"))
div = int(input("Digite um divisor"))
print(restoDivisao(5,2))