def fatorial(num):
	if num == 0:
		fat = 1
	else:
		fat = num * fatorial(num - 1)
	return fat


num = 5
resultado = fatorial(num)
print(resultado)
