Hi, Hf = input().split()
Hi = int(Hi)
Hf = int(Hf)

# inicio
if Hf > Hi:
    tempoJ = Hf - Hi

elif Hf < Hi:
    tempoJ = 24 - Hi
    tempoJ += Hf

else:
    tempoJ = 24

print("O JOGO DUROU {0} HORA(S)".format(tempoJ))