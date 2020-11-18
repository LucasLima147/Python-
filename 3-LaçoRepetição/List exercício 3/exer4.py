cont = 1 
H = 0
N = int(input("Digite um valor de até aonde deseje somar: "))
if N > 0:
    while cont <= N:
        H = H + (1 / cont)
        cont = cont + 1
    print(H)