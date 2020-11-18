Alimento = int(input("Digite um código de 1 a 15: "))
if Alimento > 0 and Alimento <= 15:
    if Alimento == 1:
        print("Alimento Não-precíveis")
    elif Alimento <= 4: 
        print("Alimento Perecível")
    elif Alimento <= 6:
        print("Vestuário")
    elif Alimento == 7:
        print("Higiene Pessoal")
    elif Alimento <= 15:
        print("Limpeza e Utensílios Domésticos")
else:
    print("Código Inválido")