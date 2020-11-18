cont1 = 1

while cont1 <= 6:
    cont2 = 1
    #inicio do cont 1
    while cont2 <= 6:
        #inicio do cont 2
        if (cont1+cont2) == 7:
            print(cont1, cont2)
        cont2 = cont2 + 1
        #fim do cont 2

    cont1 = cont1 + 1
    #fim do cont 1