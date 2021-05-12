import random

numErros = -1
partesDoCorpo = ["O", "|", "/", "\\", "/", "\\"]
partesDoCorpoParaDesenhar = [" ", " ", " ", " ", " ", " ", " "]
letrasCorretas = []
letrasIncorretas = []


def sortearPalavra():
    with open("palavras.txt", "r") as arquivo:
        palavras = arquivo.read().replace("\n", ",").split(",")
        return palavras[random.randint(0, len(palavras)-1)]


def desenhaCorpo(numErros):
    numErros += 1
    partesDoCorpoParaDesenhar[numErros] = partesDoCorpo[numErros]
    return 1


def desenhaForca(palavra):
    print(" +---+")
    print(" |   |")
    print(" %s   |" % partesDoCorpoParaDesenhar[0])
    print("%s%s%s  |" %
          (partesDoCorpoParaDesenhar[1], partesDoCorpoParaDesenhar[2], partesDoCorpoParaDesenhar[3]))
    print("%s%s   |" %
          (partesDoCorpoParaDesenhar[4], partesDoCorpoParaDesenhar[5]))
    print("     |")
    print("*********** \n\n")


def verificaLetraDigitada(word, letra):
    print("A palavra é: ", end="")
    for i in range(len(word)):
        print("_ ", end="")
    print("\n \n", end="\n")


def jogo():
    gameOver = False
    word = sortearPalavra()
    while not gameOver:
        desenhaForca(word)
        verificaLetraDigitada(word, "")
        gameOver = True


jogo()
