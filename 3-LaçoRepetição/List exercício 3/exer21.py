#variaveis pr-e definidas
para = 0 
maior_idade = 0 
habitantes = 0 
feminino = 0 
#ainda teremos as varivaeis olhos, cabelos e sexo, perc_feminino

print("Para parar a execução do código, digite -1")
while para != -1:
    sexo = input("Digite seu sexo, sendo: \nM para masculino\nF para femino\n Resposta: ")
    if sexo == "M":
        idade = int(input("Digite sua idade: "))
        habitantes = habitantes + 1
        #Varifica maior idade
        if maior_idade >= idade:
            maior_idade = idade
    elif sexo == "F":
        idade = int(input("Digite sua idade: "))
        #Varifica maior idade
        if maior_idade >= idade:
            maior_idade = idade
        olhos = input("Digite a cor dos seus olhos, sendo:\nA para azuis\nV para verdes\nC para castanhos\n Resposta: ")
        cabelos = input("Digite a cor dos seus olhos, sendo:\nL para loiros\nP para pretos\nC para castanhos\n Resposta: ")
        if idade >= 18 and idade <= 35 and olhos == "V" and cabelos == L:
            feminino = feminino + 1
    else:
        print("sexo inválido")
    
    para = int(input("Deseja parar: "))

perc_feminino = feminino/(habitantes * 100)
print(perc_feminino)
print(maior_idade)