#Primeiro eemplo de IF ELSE(SE e SENÂO)

N1 = int(input("Primeira Nota: "))
N2 = int(input("Segunda Nota: "))

Media = (N1+N2)/2
if Media >= 70:
    print("aprovado ", Media)
else:
    if Media >= 30:
        if Media >= 55:
            print("Aprovado, porem de Exame ", Media)
        else:
            print("Reprovado mesmo com exame ", Media)
    else:
        print("reprovado ", Media)
