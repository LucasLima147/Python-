cont = 1
# sexo
homem = 0
mulher = 0
# alturas
Alt_homem = 0.0
Alt_mulher = 0.0
# altura maior e menor
maior_homem = 0
menor_homem = 0
maior_mulher = 0 
menor_mulher = 0 

# Para calcular a altura média das mulheres
Soma_altura_mulher = 0 

while cont <= 50:
    sexo = input("Digite M (masculino) e F (Feminino): ")

    if sexo == "M":
        homem = homem + 1
        Alt_homem = float(input("Digite sua altura"))
        # verifica se é maior ou menor
        if Alt_homem >= maior_homem:
            maior_homem = Alt_homem
        elif Alt_homem >= menor_homem:
            menor_homem = Alt_homem
        cont = cont + 1
    elif sexo == "F":
        mulher = mulher + 1
        Alt_mulher = float(input("Digite sua altura"))
        #soma da altura de mulheres
        Soma_altura_mulher = Soma_altura_mulher + Alt_mulher

        # verifica se é maior ou menor
        if Alt_mulher >= maior_mulher:
            maior_mulher = Alt_mulher
        elif Alt_mulher >= menor_mulher:
            menor_mulher = Alt_mulher
        cont = cont + 1
    else:
        print("sexo inválido")

# resultados
print("A Altura maior e menor entre: \n Homens: ", maior_homem, menor_homem, " \n Mulheres: ", maior_mulher, menor_mulher)
print(Soma_altura_mulher/mulher)
print("Numero de Homen: ", homem)

# percentuais
per_homem = (homem / 50) * 100
per_mulher = (mulher / 50) * 100
dif_percentual = per_homem - per_mulher
print("A diferença de percentual entre homens e as mulheres é: ", dif_percentual)