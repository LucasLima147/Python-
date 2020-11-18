from os import system

def incluirContato(contatos, nome):
    contatos.append(nome)
    print("Contato adicionado com sucesso")
    system("pause")

def consultatContato(contatos, consulta):
    if consulta in contatos:
        print("Contatos existe na lista")
        system("pause")
    else:
        print("Contatos não existe na lista")
        system("pause")

def listarContatosCrescente(contatos):
    print()
    contatosCrescente = sorted(contatos)
    for pessoa in contatosCrescente:
        print(pessoa)
    system("pause")

def listarContatosDecrescente(contatos):
    print()
    contatosDescrescente = sorted(contatos, reverse=True)
    for pessoa in contatosDescrescente:
        print(pessoa)
    system("pause")
    

def listarContatos(contatos, qtd_lista):
    print()
    if len(conatos) <= qtd_lista:
        for i in range(qtd_lista):
            print(conatos[i])
    else:
        print("A quantidade deseja excede a quantidade de contatos existente")
    system("pause")

def removerContato(contatos, removerContato):
    if removerContato in contatos:
        contatos.remove(removerContato)
        print("pessoa removida com sucesso")
    else:
        print("Essa pessoa não existe na lista de contatos")
    system("pause")


listaDeContatos= []
opcao = 0
while opcao != 7:
    system("cls")
    print("programa de Contatos\nEscolha uma das opções abaixo:")
    print("1 - novo contato;")
    print("2 - consultar contato;")
    print("3 - listar contatos em ordem crescente;")
    print("4 - listar contatos em ordem decrescente;")
    print("5 - listar uma quantidade de contatos;")
    print("6 - remover um contato;")
    print("7 - Sair")
    opcao = int(input("\nDigite a opção desejada: "))
    if opcao > 7 or opcao < 1:
        print("opção inválida")
    else:
        if opcao == 1:
            nome = input("Digite o nome do contato que deseja incluir: ")
            incluirContato(listaDeContatos, nome)
        elif opcao == 2:
            consulta = input("Contato a ser consultado: ")
            consultatContato(listaDeContatos, consulta)
        elif opcao == 3:
            listarContatosCrescente(listaDeContatos)
        elif opcao == 4:
            listarContatosDecrescente(listaDeContatos)
        elif opcao == 5:
            qtd_contatos = int(input("digite a quantidade de contatos que deseja listar: "))
            listarContatos(listaDeContatos, qtd_contatos)
        elif opcao == 6:
            nome_remover = input("Contato que deseja remover: ")
            removerContato(listaDeContatos, nome_remover)
        elif opcao == 7:
            print("\nObrigado por usar o nosso programa")