n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

vet = [n1, n2, n3]
vet.sort()
print("{0}\n{1}\n{2}".format(vet[0], vet[1], vet[2]))
print()
print("{0}\n{1}\n{2}".format(n1, n2, n3))