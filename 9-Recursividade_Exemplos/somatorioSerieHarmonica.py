def somatorioHarmonico(divisor):
	if divisor == 1:
		aux = 1
	else:
		aux = (1/divisor) + somatorioHarmonico(divisor-1)

	return aux


print(somatorioHarmonico(998))