#variaveis que usaremos para a porcentagem
periodo = int(input("Digite o periodo(em meses) para a estimativa: "))
N_nasci = int(input("Nº de crianças nascidas no periodo: "))
N_mortas = 0
N_mortas_periodo = 0
N_mort_per_masc = 0
cri_masc = 0
cri_femi = 0

#para começar o while 
print("para parar o programa, digite X ao pedir o sexo da criança \n")
sexo = input("Digite o sexo da criança falecida, sendo M(para masculino)ou F(para feminino)")
while sexo != 'X':
    #diferenciando sexo para contagem
    if sexo == "M":
        N_mortas = N_mortas + 1
        T_vida = int(input("Digite o tempo de vida da criança em meses: "))
        if T_vida <= periodo or T_vida <= 24: # 24 meses = 2 anos
            N_mortas_periodo = N_mortas_periodo + 1
            N_mort_per_masc = N_mort_per_masc + 1
    elif sexo == "F":
        N_mortas = N_mortas + 1
        T_vida = int(input("Digite o tempo de vida da criança em meses: "))
        if T_vida <= periodo or T_vida <= 24:
            N_mortas_periodo = N_mortas_periodo + 1
    
    #para a repetição
    sexo = input("Digite o sexo da criança falecida, sendo M(para masculino)ou F(para feminino)")

#variaveis de porcentagem
porcentagem1 = N_mortas/(N_nasci*100)
porcentagem2 = N_mort_per_masc/(N_nasci*100)
porcentagem3 = N_mortas_periodo/(N_nasci*100)

print(porcentagem1)
print(porcentagem2)
print(porcentagem3)