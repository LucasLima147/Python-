S = 0
cont = 1
sinal = 1

while cont <= 10:
    S = S + (sinal * (cont / (cont * cont)))
    
    cont = cont + 1
    sinal = sinal * -1
    
print(S)