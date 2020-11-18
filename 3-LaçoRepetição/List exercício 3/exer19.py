# Variaveis geral
# cod_emp nós vamos pegar direto
cod_emp = 0
N_func = 0

'''========================================================'''
# Variaveis de cada categoria
N_func_maior_grande = 0
N_func_maior_media = 0
N_func_maior_pequena = 0
N_func_maior_micro = 0

cod_emp_maior_grande = 0
cod_emp_maior_media = 0
cod_emp_maior_pequena = 0
cod_emp_maior_micro = 0 
'''========================================================'''
print("Para parar a verificação, digite o código da empresa como 0")

cod_emp = int(input("Digite o código da empresa: "))
while cod_emp != 0:
    categoria = input("digite a categoria da sua empresa(grande, media, pequena ou micro): ")
    if categoria == "grande":
        N_func = int(input("Digite o Nº de funcionários da empresa: "))
        #verifica se é a maior dessa categoria
        if N_func >= N_func_maior_grande:
            N_func_maior_grande = N_func
            cod_emp_maior_grande = cod_emp
    elif categoria == "media":
        N_func = int(input("Digite o Nº de funcionários da empresa: "))
        #verifica se é a maior dessa categoria
        if N_func >= N_func_maior_media:
            N_func_maior_media = N_func
            cod_emp_maior_media = cod_emp
    elif categoria == "pequena":
        N_func = int(input("Digite o Nº de funcionários da empresa: "))
        #verifica se é a maior dessa categoria
        if N_func >= N_func_maior_pequena:
            N_func_maior_pequena = N_func
            cod_emp_maior_pequena = cod_emp
    elif categoria == "micro":
        N_func = int(input("Digite o Nº de funcionários da empresa: "))
        #verifica se é a maior dessa categoria
        if N_func >= N_func_maior_micro:
            N_func_maior_micro = N_func
            cod_emp_maior_micro = cod_emp
    else:
        print("categoria inválida")
    
    cod_emp = int(input("Digite o código da empresa: "))

print("O Codigo e o Nº de funcionarios da maior empresa de cada categoria é: ")
print("GRANDE: ", cod_emp_maior_grande, N_func_maior_grande)
print("MEDIA: ", cod_emp_maior_media, N_func_maior_media)
print("PEQUENA: ", cod_emp_maior_pequena, N_func_maior_pequena)
print("MICRO: ", cod_emp_maior_micro, N_func_maior_micro)