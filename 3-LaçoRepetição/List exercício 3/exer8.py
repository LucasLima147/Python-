cont = 1 
sinal = 1 
H = 0.0
while cont <= 10:
	H = (sinal * (1/((2*cont-1)**3))) + H
	cont = cont + 1
	sinal = sinal * -1

PI = 3 / (H * 3)
print(PI)