T1 = int(input("Tipo 1. Digite: \n 1 - marífero \n 2 - aves \n 3 - répteis \n sua opção: "))

# Mamifero
if T1 == 1:
    T2 = int(
        input("Tipo 2. Digite:\n 1 - quadrúpedes \n 2 - Bípedes \n 3 - Voador \n 4 - aquatico \n sua opção: "))
    if T2 == 1:
        T3 = int(input("Tipo 3. Digite:\n 1 - carnívoro \n  2 - herbívoro \n sua opção: "))
        if T3 == 1:
            print("Leão")
        elif T3 == 2:
            print("Cavalo")
        else:
            print("Tipo 3 inválido")

    elif T2 == 2:
        T3 = int(input("Tipo 3. Digite:\n 1 - Onívoro \n  2 - frutífero \n sua opção: "))
        if T3 == 1:
            print("Homem")
        elif T3 == 2:
            print("Macaco")
        else:
            print("Tipo 3 inválido")
    elif T2 == 3:
        print("Morcego")
    elif T2 == 4:
        print("Baleia")
    else:
        print("Tipo 2 inválido")

# Aves
elif T1 == 2:
    T2 = int(input("Tipo 2. Digite: \n 1 - Não voadores \n 2 - Nadadores \n 3 - De rapina \n sua opção: "))

    if T2 == 1:
        T3 = int(input("Tipo 3. Digite:\n 1 - Tropical \n  2 - Polar \n sua opção: "))
        if T3 == 1:
            print("Avestruz")
        elif T3 == 2:
            print("Pinguim")
        else:
            print("Tipo 3 inválido")
    elif T2 == 2:
        print("Pato")
    elif T2 == 3:
        print("Águia")
    else:
        print("Tipo 2 inválido")

# Repteis
elif T1 == 3:
    T2 = int(input("Tipo 2. Digite:\n 1 - Com Casto \n 2 - Carnívoros \n 3 - Sem Patas \n sua opção: "))
    if T2 == 1:
        print("Tartaruga")
    elif T2 == 2:
        print("Crocodilo")
    elif T2 == 3:
        print("Cobra")
    else:
        print("Tipo 2 inválido")
else:
    print("Tipo 1 de animal inválido")
