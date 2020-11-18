def posicao(cadeia, subcadeia):
    achou = 0
    tamc = len(cadeia)
    tams = len(subcadeia)

    if(tamc > tams):
        inicio = 0
        while (tamc > tams) and (achou == 0):
            i = 0
            j = inicio
            if subcadeia[i] == cadeia[j]:
                local = j
                i += 1
                j += 1
                while (i < tams) and (subcadeia[i] == cadeia[j]):
                    i += 1
                    j += 1
                if i < tams:
                    inicio += 1
                    tamc -= 1
                else:
                    achou = 1
            else:
                inicio += 1
                tamc -= 1
    else:
        print("A subcadeia tem tamanho Maior que a cadeia!")
    
    if(achou == 0):
        local = -1
    
    print(local)
####################################

cadeia, subcadeia = input("Digite a cadeia e a subcadeia: ").split()
posicao(cadeia, subcadeia)