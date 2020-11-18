from math import sqrt

A = int(input("n1: "))
B = int(input("n2: "))
C = int(input("n3: "))

Del = (B**2)-(4*A*C)
if Del > 0:
    R1 = (-B+sqrt(Del))/2*A
    R2 = (-B-sqrt(Del))/2*A
    print("As raizes da esqueção são: ", R1, R2)
else:
    print("Não existe raiz Raiz de Delta negativo, por isso, não existe Raiz da equação")