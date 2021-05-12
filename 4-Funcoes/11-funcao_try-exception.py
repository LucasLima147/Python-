"""
Para o tratamentos de erros e/ou exceções, temos a função try except
    Forma de uso:
        try:
            tenta exercutar um trecho de código
        except:
            tratamento caso ocorra uma exceção
        else:
            se não houver nenhum erro ou exceção
        finally:
            forçar a execução de um trecho de código, mesmo que ocorra um erro
"""

# Exemplo 1 - try except
try:
    X = 8 + "s"
    print("Soma feita com sucesso")
except TypeError:
    print("Erro na adção")


# Exemplo 2 - try except else
try:
    arq = open("testeError.txt", "w")
    arq.write("Tste do try")
except IOError:
    print("\nErro de escrita no arquvio")
else:
    print("\nEscrita realizada com sucesso")

# Exemplo 2 - try except else (com erro agora)
try:
    arq = open("testeError", "r")
except IOError:
    print("\nErro de leitura do arquivo")
else:
    print("\nEscrita realizada com sucesso")

# Exemplo 3 - try except else finally
try:
    arq = open("testeError.txt", "w")
    arq.write("Tste do try")
except IOError:
    print("\nErro de escrita no arquvio ou arquivo não encontrado")
else:
    print("\nEscrita realizada com sucesso")
finally:
    print("Tentativa de escrita no arquivo finalizada")

# Exemplo 3 - try except else finally (com erro)
try:
    arq = open("testeError", "r")
except IOError:
    print("\nErro de leitura no arquvio")
else:
    print("\nEscrita realizada com sucesso")
finally:
    print("Tentativa de leitura no arquivo finalizada")

# EXEMPLO PRÁTIVO PARA TRATAR ERROS
def askint():
    while True:
        try:
            num = int(input("\nPor gentileza, digite um número: "))
        except:
            print("Você não digitou um número!")
            continue
        else:
            print("Obrigado pelo número!")
            break
        finally:
            print("fim de execução")
        
        print(num)
askint()

# EXEMPLO PRÁTIVO PARA MOSTRAR O ERRO
tupla = (1,2,3,4,5)
try:
    tupla.append(5)
except AttributeError as e:
    print("erro de atributo:", e)
except IOError as e:
    print("erro de IO:", e)