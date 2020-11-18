print("para sair digite 0 ")
voto = int(input("vote: "))
voto_branco = 0
voto_nulo = 0
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
num_voto = 0
while voto != 0:
    voto = int(input("vote: "))
    if voto == 6:
        print("voto em branco")
        voto_branco = voto_branco + 1
        num_voto = num_voto + 1
    elif voto == 5:
        print("voto nulo")
        voto_nulo = voto_nulo + 1
        num_voto = num_voto + 1
    elif voto == 4:
        print("votou no candidato 4")
        candidato4 = candidato4 + 1
        num_voto = num_voto + 1
    elif voto == 3:
        print("votou no candidato 3")
        candidato3 = candidato3 + 1
        num_voto = num_voto + 1
    elif voto == 2:
        print("votou no candidato 2")
        candidato2 = candidato2 + 1
        num_voto = num_voto + 1
    elif voto == 1:
        print("votou no candidato 1")
        candidato1 = candidato1 + 1
        num_voto = num_voto + 1
    else:
        print("voto inválido")

print(candidato1)
print(candidato2)
print(candidato3)
print(candidato4)
print(voto_branco)
print(voto_nulo)
print((voto_branco)/num_voto * 100)
print((voto_nulo)/num_voto * 100)