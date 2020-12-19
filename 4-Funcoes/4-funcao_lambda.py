"""
    A função lambda é utilizado como forma de simplificar funções que usa, apenas 1 linha de código
        também conhecida como função anonima, é utilizada da seguinte forma:
            var = lambda parametros: operação
            var(valor) 
"""
# Calculo de potência
potencia = lambda num: num**2
print("A potência é:", potencia(5))

# Condicional
par = lambda num: (num % 2) == 0
print("primeiro teste:", par(5))
print("segundo teste:", par(4))

# Primeira letra da String
first = lambda literal: literal[0]
print("A primeira leta da palabra 'Python' é:", first("Python"))

# Invertendo a String
reverso = lambda palavra: palavra[::-1]
print("A palabra 'Python' invertido é:", reverso("Python"))

# 2 parametros / adção
soma = lambda x,y: x+y
print("A soma delos valores é:", soma(2, 3))