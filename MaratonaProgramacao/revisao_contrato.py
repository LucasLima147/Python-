while True:
    dig, num = input().split()
    if dig == num:
        break
    else:
        lista = num.split(dig)
        lista = "".join(lista)
        if not lista:
            print("0")
        
        lista = int(lista)
        if lista == 0:
            print("0")
        else:
            print(lista)