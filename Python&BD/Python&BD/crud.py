#Função para realizar uma CONSULTA no BD
def select(fields, tables, cursor, where=None):

	#SQL do SELECT
	query = f"SELECT {fields} FROM {tables}"
	if where:
		query += f" WHERE {where}"

	#execução e retorno do resultado do comando SQL
	cursor.execute(query)
	return cursor.fetchall()

#Função Para realizar uma INSERÇÃO no BD
def insert(values, table, cursor, conexao, fields=None):

	query = f"INSERT INTO {table}"

	#verifica irá inserir em colunas específicas
	if fields:
		query += f" ({fields}) "

	#colocando os valores a serem inseridos
	#Values(...),(...),(...)
	#join(["(" + v + ")"  for v in values]) -> lista interativa
	query += " VALUES" + ",".join(["(" + v + ")"  for v in values]) + ";" 

	#Execução do comando SQL
	cursor.execute(query)
	#Usamos o .commit() na variavel de conexão com o BD para garantir a execução e efetivação do comando SQL
	return conexao.commit()

#realizando uma ATUALIZAÇÃO no BD
def update(table, sets, cursor, conexao, where=None):

	query = f"UPDATE {table} SET " + ",".join([f"{field} = '{value}'" for field, value in sets.items()])
	if where:
		query += f" WHERE {where};"

	cursor.execute(query)
	return conexao.commit()

def delete(table, where, cursor, conexao):

	query = f"DELETE FROM {table} WHERE {where}"
	cursor.execute(query)
	return conexao.commit()