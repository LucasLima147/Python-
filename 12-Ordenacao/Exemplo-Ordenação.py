import random
import os

""" módulos """


def criar_vetor():
    tam_vetor = 100
    vetor = [0] * tam_vetor
    cont = 0
    while cont < tam_vetor:
        valor = random.randint(0, 100000)
        vetor[cont] = valor
        cont += 1
    return vetor


def listar_vetor(vetor):
    print("Os 20 primeiros números do vetor são: ")
    cont = 0
    while cont < 20:
        print(vetor[cont], end=", ")
        cont += 1


def selection_sort(vetor):
    cont = 1
    while cont < len(vetor):
        for i in range(len(vetor)):
            menor = i
            for j in range(i+1, len(vetor)):
                if vetor[j] < vetor[menor]:
                    menor = j

            aux = vetor[i]
            vetor[i] = vetor[menor]
            vetor[menor] = aux
        cont += 1


def inserction_sort(vetor):
    vetor_insere = [vetor.pop(0)]
    while len(vetor) != 0:
        aux = vetor.pop(0)
        index = 0
        flag = 0
        while flag == 0 and index < len(vetor_insere):
            if(aux < vetor_insere[index]):
                flag = 1
            index += 1

        if flag != 0:
            vetor_insere.insert(index-1, aux)
        else:
            vetor_insere.append(aux)

    vetor.extend(vetor_insere)


def shell_sort(vetor):
    i = len(vetor)//2
    while i != 0:
        chave = True
        while chave:
            for k in range(len(vetor)-i):
                if(vetor[k] > vetor[k+i]):
                    aux = vetor[k]
                    vetor[k] = vetor[k+i]
                    vetor[k+i] = aux
                    chave = False
        i = i // 2


def buble_sort(vetor):
    flag = True
    while flag:
        flag = False
        index = 0
        while index < len(vetor)-1:
            if(vetor[index] > vetor[index+1]):
                aux = vetor[index+1]
                vetor[index+1] = vetor[index]
                vetor[index] = aux
                flag = True
            index += 1


def quick_sort(vetor, inicio, fim):
    i = inicio
    j = fim
    meio = vetor[(inicio+fim)//2]
    while j > i:
        while vetor[i] < meio:
            i += 1
        while vetor[j] > meio:
            j -= 1

        if(i <= j):
            aux = vetor[i]
            vetor[i] = vet[j]
            vet[j] = aux
            i += 1
            j -= 1
    if inicio < j:
        quick_sort(vetor, inicio, j)
    if i < fim:
        quick_sort(vetor, i, fim)


#######################################################################################
""" MAIN """

vet = criar_vetor()
sair = False
while not sair:
    os.system("cls")
    print("******* ORDENAÇÃO *******")
    print("Escolha o que deseja fazer")
    print("1 - Criar um novo vetor")
    print("2 - Seleção Direta")
    print("3 - Inserção Direta")
    print("4 - Shell Sort")
    print("5 - Buble Sort")
    print("6 - Quick Sort")
    print("7 - Listar Vetor")
    print("8 - Sair")
    opcao = int(input("\nDigite uma opcao do menu: "))

    if opcao == 1:
        vet = criar_vetor()
        print("vetor criado")
        os.system("pause")
    elif opcao == 2:
        selection_sort(vet)
        print("Seleção Direta realizada com sucesso")
        os.system("pause")
    elif opcao == 3:
        inserction_sort(vet)
        print("Inserção Direta")
        os.system("pause")
    elif opcao == 4:
        shell_sort(vet)
        print("Shell Sort realizado com sucesso")
        os.system("pause")
    elif opcao == 5:
        buble_sort(vet)
        print("Buble Sort realizado com sucesso")
        os.system("pause")
    elif opcao == 6:
        quick_sort(vet, 0, len(vet)-1)
        print("Quick Sort realizado com sucesso")
        os.system("pause")
    elif opcao == 7:
        listar_vetor(vet)
        os.system("pause")
    elif opcao == 8:
        sair = True
    else:
        print("opção inválida")

