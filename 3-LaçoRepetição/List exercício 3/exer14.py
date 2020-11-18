n1 = int(input("N1: "))
n2 = int(input("N2: ")) 

while n1 <= n2:
    primo = 0
    cont = 1
    while cont <= n1:
        # % == MOD == resto
        if (n1 % cont) == 0:
            primo = primo + 1
        cont = cont + 1
    
    if primo == 2:
        print(n1)
    n1 = n1 + 1