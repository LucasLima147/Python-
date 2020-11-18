def binario(numero):
	if numero//2 < 1:
		aux = str(numero % 2)
	else:
		aux = binario((numero // 2)) + str(numero % 2)

	return aux

numero = 22
print(binario(numero))