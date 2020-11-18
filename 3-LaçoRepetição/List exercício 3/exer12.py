num_ant = 0
num = 1
print(num_ant, num)

cont = 1
while cont <= 18:
    prox = num_ant + num
    num_ant = num
    num = prox
    print(prox)
    
    cont = cont + 1