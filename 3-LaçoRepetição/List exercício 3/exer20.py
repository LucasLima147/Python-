# variaveis iniciais
sal_minimo = float(input("Digite o valor do Salário minimo atual: "))
impos_renda = 0.0
cont = 1
while cont <= 10:
    # Varivais
    cpf = input("Digite seu CPF: ")
    N_dependente = int(input("Digite o numero de dependentes: "))
    renda = float(input("Digite o valor da renda: "))
    desconto = 0.0
    sal_min_final = 0.0
    V_liquido = 0

    desconto = N_dependente * 0.05
    desconto = sal_minimo * desconto
    sal_min_final = sal_minimo - desconto
    aliquota = renda // sal_min_final

    if aliquota > 7:
        impos_renda = renda * 0.20
    elif aliquota > 5 and aliquota <= 7:
        impos_renda = renda * 0.15
    elif aliquota > 3 and aliquota <= 5:
        impos_renda = renda * 0.10
    elif aliquota > 2 and aliquota <= 3:
        impos_renda = renda * 0.05
    else: 
        impos_renda = 0
    
    print("O valor do Imposto de renda da pessoa de CPF ", cpf, ", é de: ", impos_renda, ",00 reais\n")
    
