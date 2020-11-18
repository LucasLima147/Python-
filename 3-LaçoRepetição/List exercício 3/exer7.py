num = 2
den = 500
sinal = 1
soma = 0 

while den > 0:
    if num == 2:
        soma = soma + (sinal * (num/den))
        num = 5
    else: 
        soma = soma + (sinal * (num/den))
        num = 2
    # Troca
    sinal = sinal * -1
    den = den - 50
print(soma)
