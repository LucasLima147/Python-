X, Y = input().split()
X = float(X)
Y = float(Y)

if X == Y == 0:
    print("Origem")
elif X == 0 and not (Y == 0):
    print("Eixo Y")
elif Y == 0 and not (X == 0):
    print("Eixo X")
else:
    if X > 0:
        if Y > 0:
            print("Q1")
        else:
            print("Q4")
    else:
        if Y > 0:
            print("Q2")
        else:
            print("Q3")