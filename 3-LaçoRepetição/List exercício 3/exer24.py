# variaveis pré-definidas
usuarios = 0
#elevadores
elevA = 0
elevB = 0
elevC = 0
# Periodos e periodos do elevador
peri_matu = 0
elevA_periM = 0
elevB_periM = 0
elevC_periM = 0
#---------------
peri_vesp = 0
elevA_periV = 0
elevB_periV = 0
elevC_periV = 0
#----------------
peri_nort = 0
elevA_periN = 0
elevB_periN = 0
elevC_periN = 0
# Ainda teremos as variaveis: elevador, periodo, perc_elevA, perc_elevB, perc_elevC
print("Para parar o sistema: digite PARAR")
parar = "Continua"
while parar != "PARAR": #Não sei a condição de parada, por isso usei essa condição
    usuarios = usuarios + 1
    # elevador
    elevador = input("Qual elevador você mais utiliza entre A, B ou C? \n R: ")
    # ELEVADOR A
    if elevador == "A":
        elevA = elevA + 1
        periodo = input("Digite o perido que mais utiliza esse elevador, sendo: \n M para matutino;\n V para vespertino;\n N para noturno.\n R: ")
        #perido de utilização desse elevador
        if periodo == "M":
            peri_matu = peri_matu + 1
            elevA_periM = elevA_periM + 1
        elif periodo == "V":
            peri_vesp = peri_vesp + 1
            elevA_periV = elevA_periV + 1
        elif periodo == "N":
            peri_nort = peri_nort + 1
            elevA_periN = elevA_periN + 1
    # ELEVADOR B
    elif elevador == "B":
        elevB = elevB + 1
        periodo = input("Digite o perido que mais utiliza esse elevador, sendo: \n M para matutino;\n V para vespertino;\n N para noturno.\n R: ")
        #perido de utilização desse elevador
        if periodo == "M":
            peri_matu = peri_matu + 1
            elevB_periM = elevB_periM + 1
        elif periodo == "V":
            peri_vesp = peri_vesp + 1
            elevB_periV = elevB_periV + 1
        elif periodo == "N":
            peri_nort = peri_nort + 1
            elevB_periN = elevB_periN + 1
    # ELEVADOR C
    elif elevador == "C":
        elevC = elevC + 1
        periodo = input("Digite o perido que mais utiliza esse elevador, sendo:\n M para matutino;\n V para vespertino;\n N para noturno.\n R: ")
        #perido de utilização desse elevador
        if periodo == "M":
            peri_matu = peri_matu + 1
            elevC_periM = elevC_periM + 1
        elif periodo == "V":
            peri_vesp = peri_vesp + 1
            elevC_periV = elevC_periV + 1
        elif periodo == "N":
            peri_nort = peri_nort + 1
            elevC_periN = elevC_periN + 1
    
    parar = input("deseja parar: ")

""" Primeiro Calculo """
#Matutino
if peri_matu >= peri_vesp and peri_matu >= peri_nort:
    print("O periodo de maior fluxo é o Matutino")
    """ Segundo Calculo caso seja Matutino"""
    #elevadores desse período
    if elevA_periM >= elevB_periM and elevA_periM >= elevC_periM:
        print("O elevador mais usado nesse periodo é o A")
    elif elevB_periM >= elevA_periM and elevB_periM >= elevC_periM:
        print("O elevador mais usado nesse periodo é o B")
    elif elevC_periM >= elevA_periM and elevC_periM >= elevB_periM:
        print("O elevador mais usado nesse periodo é o B")
#Vespertino
elif peri_vesp >= peri_matu and peri_vesp >= peri_nort:
    print("O perio de maior fluxo é o Vespertino")
    """ Segundo Calculo caso seja Vespertino"""
    #elevadores desse período
    if elevA_periV >= elevB_periV and elevA_periV >= elevC_periV:
        print("O elevador mais usado nesse periodo é o A")
    elif elevB_periV >= elevA_periV and elevB_periV >= elevC_periV:
        print("O elevador mais usado nesse periodo é o B")
    elif elevC_periV >= elevA_periV and elevC_periV >= elevB_periV:
        print("O elevador mais usado nesse periodo é o C")
#Noturno
elif peri_nort >= peri_matu and peri_nort >= peri_vesp:
    print("O periodo de maior fluxo é o Noturno")
    """ Segundo Calculo caso seja Noturno"""
    #elevadores desse período
    if elevA_periN >= elevB_periN and elevA_periN >= elevC_periN:
        print("O elevador mais usado nesse periodo é o A")
    elif elevB_periN >= elevA_periN and elevB_periN >= elevC_periN:
        print("O elevador mais usado nesse periodo é o B")
    elif elevC_periN >= elevA_periN and elevC_periN >= elevB_periN:
        print("O elevador mais usado nesse periodo é o C")

if elevA >= elevB and elevA >= elevC:
    print("O elevador A é o mais utilizado\n")
elif elevB >= elevA and elevB >= elevC:
    print("O elevador B é o meis utilizado\n")
elif elevC >= elevA and elevC >= elevB:
    print("O elevador C é o mais utilizado\n")

""" Terceiro Calculo """
#percentagem
perc_elevA = (elevA / usuarios) * 100
perc_elevB = (elevB / usuarios) * 100
perc_elevC = (elevC / usuarios) * 100

if perc_elevA >= perc_elevB and perc_elevA >= perc_elevC:
    if perc_elevB < perc_elevC:
        print("A diferença de percentual entre o mais utilizado e o menor utilizado é de :", perc_elevA - perc_elevB)
        """ Quarto Calculo"""
        print("o percentual do elevador de média utilização é de: ", perc_elevC)
    else:
        print("A diferença de percentual entre o mais utilizado e o menor utilizado é de :", perc_elevA - perc_elevC)
        """ Quarto Calculo"""
        print("o percentual do elevador de média utilização é de: ", perc_elevB)
elif perc_elevB >= perc_elevA and perc_elevB >= perc_elevC:
    if perc_elevA < perc_elevC:
        print("A diferença de percentual entre o mais utilizado e o menor utilizado é de :", perc_elevB - perc_elevA)
        """ Quarto Calculo"""
        print("o percentual do elevador de média utilização é de: ", perc_elevC)
    else:
        print("A diferença de percentual entre o mais utilizado e o menor utilizado é de :", perc_elevB - perc_elevC)
        """ Quarto Calculo"""
        print("o percentual do elevador de média utilização é de: ", perc_elevA)
else: #para cair nesse caso, é comprovado que o C é maior que todos
    if perc_elevA < perc_elevB:
        print("A diferença de percentual entre o mais utilizado e o menor utilizado é de :", perc_elevC - perc_elevA)
        """ Quarto Calculo"""
        print("o percentual do elevador de média utilização é de: ", perc_elevB)
    else:
        print("A diferença de percentual entre o mais utilizado e o menor utilizado é de :", perc_elevC - perc_elevB)
        """ Quarto Calculo"""
        print("o percentual do elevador de média utilização é de: ", perc_elevA)
