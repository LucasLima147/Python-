#variaveis pré-definidas para o programa
qtd_otimo = 0
qtd_bom = 0
qtd_regular = 0
qtd_ruim = 0
qtd_pessimo = 0
med_idade_r = 0
maior_idade_o = 0
maior_idade_r = 0
maior_idade_p = 0

cont = 0
while cont <= 100:
    idade = int(input("Digite sua idade: "))
    opiniao = input("Sua opniao entre A(ótimo), B(bom), C(regular), D(ruim) e E(péssimo): ")
    if opiniao == "A":  #otimo
        qtd_otimo = qtd_otimo + 1
        cont = cont + 1
        if idade <= maior_idade_o:
            maior_idade_o = idade
    elif opiniao == "B": #bom
        qtd_bom = qtd_bom + 1
        cont = cont + 1
    elif opiniao == "C": #regular
        qtd_regular = qtd_regular + 1
        cont = cont + 1
    elif opiniao == "D": #ruim
        qtd_ruim = qtd_ruim + 1
        cont = cont + 1
        if idade <= maior_idade_r:
            maior_idade_r = idade
    elif opiniao == "E": #pessimo
        qtd_pessimo = qtd_pessimo + 1
        cont = cont + 1
    else:
        print("Opção de opniao inválida, tente novamente")

#respostas do exercício
print(qtd_otimo)
print((qtd_bom+qtd_regular))