# imports
import os
import sqlite3

#remove o arquivo caso exita
os.remove("escola.db") if os.path.exists("escoladb") else None

#criando um BD
conexao = sqlite3.connect("escola.db")
#criando um cursor --> percorrer os registros
cursor = conexao.cursor()

#Comando SQL para criar uma tabela
query = 'CREATE TABLE cursos(' \
         'id integer primary key,' \
         'titulo varchar(100),' \
         'categoria varchar(140));'
#executando uma query
cursor.execute(query)

# =============================================

# Comando SQL para inserir dados em uma tabela
query = 'INSERT INTO cursos VALUES(?,?,?)'
registros = [(1000, "Ciência de Dados", "DSA"),
             (1001, "Bid Data Fundamentos", "Big Data"),
             (1002, "Python Fundamentos", "Análise de dados")]
# Executando o comando SQL e inserindo os valores na tabela
for reg in registros:
    cursor.execute(query, reg)
# grava a transação, ou seja, salvar os registros
conexao.commit()

# =============================================

# Comando SQL para fazer Seleção de registro
query = "SELECT * FROM cursos"
cursor.execute(query)                   # carrego os registros do BD
dados = cursor.fetchall()               # pego os registros retornados na forma de uma Lista de Tuplas
#mostrando no terminal os registros
for linha in dados:
    print("Curso ID: %d, Título: %s, Cateoria: %s" % linha)

# Podemos também passar o comando SQL direto no "execute()"
query = 'INSERT INTO cursos VALUES(?,?,?)'
registros = [(1003, "Gestão de Dados com MongoDB", "Bid Data"),
             (1004, "R Fundamentos", "Análise de Dados")]

for reg in registros:
    cursor.execute(query, reg)
conexao.commit()
print("\n")
cursor.execute("SELECT * FROM cursos")
dados = cursor.fetchall()
for linha in dados:
    print("Curso ID: %d, Título: %s, Cateoria: %s" % linha)

# SEMPRE feche a conexão
conexao.close()