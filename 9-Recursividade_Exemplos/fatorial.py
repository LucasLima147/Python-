def fatorial(num, fat):
	num -= 1
	if num != 0:
		fat[0] *= num
		fatorial(num, fat)
	else:
		print("Instancia Trivial foi com " + str(num))

num = 5
fat = [num]
fatorial(num, fat)
print(fat[0])
