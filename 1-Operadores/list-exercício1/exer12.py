from math import sqrt

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

Del = (B**2) - 4*A*C
R1 = ((-B + sqrt(Del))/2*A)
R2 = ((-B - sqrt(Del))/2*A)

print(R1, R2)