import random
import os
import time
from prettytable import PrettyTable

'''
OBS: fazer a importação da biblioteca PrettyTable
-> utilizei pela linha de comando no VS Code: python -m pip install -U prettytable
-> link para algumas formas de instação: https://pypi.org/project/prettytable/
'''

# Módulos


def criar_vetor():
    tam_vetor = 100000
    vetor = [0] * tam_vetor
    cont = 0
    while cont < tam_vetor:
        valor = random.randint(1, tam_vetor+1)
        vetor[cont] = valor
        cont += 1
    return vetor


def listar_vetor_primeiros(vetor):
    print("Os 20 primeiros números do vetor são: ")
    cont = 0
    while cont < 20:
        print(vetor[cont], end=" ")
        cont += 1
    print()


def listar_vetor_ultimos(vetor):
    print("Os 20 últimos números do vetor são: ")
    cont = len(vetor)-20
    while cont < len(vetor):
        print(vetor[cont], end=" ")
        cont += 1
    print("\n\n")


def relatorio_desempenho(rodadas):
    # Definindo variáveis de soma
    tp_selection = 0
    tp_inserction = 0
    tp_shell = 0
    tp_bubble = 0
    tp_quick = 0
    tt_rodadas = 0
    # gerando a primeira tabela com cada resultado
    print("Relação dos Testes\n")
    tabela = PrettyTable(["Amostras", "Selection Sort(s)", "Inserction Sort(s)",
                          "Shell Sort(s)", "Bubble Sort(s)", "Quick Sort(s)"])
    for rodada in rodadas:
        tp_selection += rodada[1]
        tp_inserction += rodada[2]
        tp_shell += rodada[3]
        tp_bubble += rodada[4]
        tp_quick += rodada[5]
        tt_rodadas += 1
        tabela.add_row(rodada)
    print(tabela)

    # definindo o tempo médio
    tp_selection = tp_selection//tt_rodadas
    tp_inserction = tp_inserction//tt_rodadas
    tp_shell = tp_shell//tt_rodadas
    tp_bubble = tp_bubble//tt_rodadas
    tp_quick = tp_quick//tt_rodadas
    # mostrando o tempo médio de cada tipo de ordenação
    print("Análise de Desempenho\n")
    tabela = PrettyTable(["tipo de Ordenação", "Selection Sort(s)"])
    tabela.add_row(["Selection Sort", tp_selection])
    tabela.add_row(["Inserction Sort", tp_inserction])
    tabela.add_row(["Shell Sort", tp_shell])
    tabela.add_row(["Bubble Sort", tp_bubble])
    tabela.add_row(["Quick Sort", tp_quick])
    print(tabela)


def selection_sort(vetor):
    inicio = time.time()
    for i in range(len(vetor)-2):
        menor = i
        for j in range(i+1, len(vetor)-1):
            if vetor[j] < vetor[menor]:
                menor = j

        aux = vetor[i]
        vetor[i] = vetor[menor]
        vetor[menor] = aux
    fim = time.time()
    print("Selection Sort concluido")
    listar_vetor_primeiros(vetor)
    return int(fim - inicio)


def inserction_sort(vetor):
    inicio = time.time()
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

    fim = time.time()
    print("Inserction Sort concluido")
    listar_vetor_primeiros(vetor)
    return int(fim - inicio)


def shell_sort(vetor):
    inicio = time.time()
    i = len(vetor)//2
    while i != 0:
        chave = False
        while not chave:
            chave = True
            for k in range(len(vetor)-i):
                if(vetor[k] > vetor[k+i]):
                    aux = vetor[k]
                    vetor[k] = vetor[k+i]
                    vetor[k+i] = aux
                    chave = False
        i = i // 2

    fim = time.time()
    print("Shell Sort concluido")
    listar_vetor_primeiros(vetor)
    return int(fim - inicio)


def buble_sort(vetor):
    inicio = time.time()
    flag = True
    while flag:
        flag = False
        for index in range(len(vetor)-1):
            if(vetor[index] > vetor[index+1]):
                aux = vetor[index+1]
                vetor[index+1] = vetor[index]
                vetor[index] = aux
                flag = True
            index += 1
    fim = time.time()
    print("Buble sort concluido")
    listar_vetor_primeiros(vetor)
    return int(fim - inicio)


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
            vetor[i] = vetor[j]
            vetor[j] = aux
            i += 1
            j -= 1
    if inicio < j:
        quick_sort(vetor, inicio, j)
    if i < fim:
        quick_sort(vetor, i, fim)

    print("Quik sort concluido")
    return int(end - init)


""" MAIN """
vet = criar_vetor()
sair = False
rodadas = []
round = 1
while not sair:
    os.system("cls")
    print("******* ORDENAÇÃO *******")
    print("Escolha o que deseja fazer")
    print("1 - Criar um novo vetor")
    print("2 - Métodos")
    print("3 - Relatório")
    print("4 - Listar os 20 primeiros")
    print("5 - Listar os 20 últimos")
    print("6 - Sair")
    opcao = int(input("\nDigite uma opcao do menu: "))

    if opcao == 1:
        vet = criar_vetor()
        print("vetor criado")
        os.system("pause")
    elif opcao == 2:
        # criando as cópias e deixando para o Quick Sort ordenar o vetor
        aux1 = vet.copy()
        aux2 = vet.copy()
        aux3 = vet.copy()
        aux4 = vet.copy()
        aux1 = selection_sort(aux1)
        aux2 = inserction_sort(aux2)
        aux3 = shell_sort(aux3)
        aux4 = buble_sort(aux4)

        init = time.time()
        quick_sort(vet, 0, len(vet)-1)
        end = time.time()
        print("Quik sort concluido")
        listar_vetor_primeiros(vet)
        tempos = [round, aux1, aux2, aux3, aux4, (end-init)]
        rodadas.append(tempos)
        print("Ordenações feitas com sucesso!")
        round += 1
        os.system("pause")
    elif opcao == 3:
        relatorio_desempenho(rodadas)
        os.system("pause")
    elif opcao == 4:
        listar_vetor_primeiros(vet)
        os.system("pause")
    elif opcao == 5:
        listar_vetor_ultimos(vet)
        os.system("pause")
    elif opcao == 6:
        sair = True
    else:
        print("opção inválida")
        os.system("pause")
