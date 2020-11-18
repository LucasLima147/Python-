mat = [[0]*10 for i in range(10)]
qtd_n = int(input())
navios = []
for X in range(qtd_n):
    di, lar, lin, col = input().split()
    di = int(di)
    lar = int(lar)
    lin = int(lin)
    col = int(col)
    nav = [di, lar, lin, col]
    navios.append(nav)
    

f = True
for nav in navios:
    lin = nav[2]-1
    col = nav[3]-1
    if nav[0] == 0:
        if col+nav[1] <= 10:
            for x in range(nav[1]):
                if mat[lin][col] != 1:
                    mat[lin][col] = 1
                    col += 1
                else:
                    f = False
                    break
        else:
            f = False
            break
    else:
        if lin+nav[1] <= 10:
            for x in range(nav[1]):
                if mat[lin][col] != 1:
                    mat[lin][col] = 1
                    lin += 1
                else:
                    f = False
                    break
        else:
            f = False
            break
if f:
    print("Y")
else:
    print("N")