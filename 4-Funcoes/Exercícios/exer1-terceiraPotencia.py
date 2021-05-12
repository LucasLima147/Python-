# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
ls = [1,2,3]
teste = list(map(lambda x: x**3, ls))
print(teste)

##############################################
teste = [x**3 for x in ls]
print(teste)