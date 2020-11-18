n1, n2, n3 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

A = max(n1, n2, n3)
if A == n1:
    B = n2
    C = n3
elif A == n2:
    B = n1
    C = n3
else:
    B = n1
    C = n2

if A >= (B+C):
    print("NAO FORMA TRIANGULO")
else:
    if (A**2) == ((B**2)+(C**2)):
        print("TRIANGULO RETANGULO")
    if (A**2) > ((B**2)+(C**2)):
        print("TRIANGULO OBTUSANGULO")
    if (A**2) < ((B**2)+(C**2)):
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if (A == C and A != B) or (B == C and B != A) or (A == B and A != C):
        print("TRIANGULO ISOSCELES")