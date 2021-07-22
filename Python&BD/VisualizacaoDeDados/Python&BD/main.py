import pymysql as bd
import crud, conexao as co

#recebendo a conexao
conn = co.conexaoBD()

"""
Cursores são estruturas de dados que indicam linha a linha de um resultado
EX: resultados de uma consulta com várias linahs da tabela
-> Sua função basicamente é organizar o resultado retornado
-> Utilizamos eles para executar o comando SQL

conn.cursor() ->em caso de tuplas de tuplas
->O retorno da função é uma TUPLA de TUPLAS
->basicamente será uma lista de listas
	->podemos salvar em uma variável e
	->acessar cada valor como um vetor/lista

Contudo, podemos ainda fazer p resultado virar um dicionarios
"""
#fazer o resultado vir como um dicionário
cursor = conn.cursor(bd.cursors.DictCursor)

#CONSULTANDO dados do BD
"""
resultado = crud.select("nome, cpf", "alunos", cursor)
print(resultado[0]["nome"])
"""
##############################################

#INSERINDO dados do BD
#sequencia: id, cpf, nome, nascimento, endereco, cidade, estado
values = ["DEFAULT, '12345678911', 'joão pedro', '2019-03-05', 'R teste BD', 'python', 'ND'",
"DEFAULT, '12345678956', 'karem rodrigues', '2019-03-05', 'R teste BD', 'python', 'ND'"]
tabela = 'alunos'
crud.insert(values, tabela, cursor, conn)
print(crud.select("*", 'alunos', cursor))

#############################################

#ATUALIZANDO dados do BD 

#sequencia: tabela, sets, cursor, conexao, where(se existir)
crud.update("alunos", {"nome": "Deidata Naruto", "cidade": "Aldeia da Folha"}, cursor, conn, "id_aluno = 2")
print(crud.select("*", 'alunos', cursor, "id_aluno = 2"))
############################################

#APAGANDO dados do BD
#sequencia: tabela, where, cursor, conexao
crud.delete("alunos", "cidade = 'Conceição do Ouros'", cursor, conn)
print(crud.select("*", 'alunos', cursor, ))