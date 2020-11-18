import pymysql as bd
"""
CONEXÃO COM O BANCO DE DADOS
->connect(host, usuario, senha, bancoDeDados, portaDeAcesso)
"""
def conexaoBD():
	host = "localhost"
	user = "root"
	password = "vertrigo"
	db = "escola"
	port = 3306
	#comando de conexão
	conn = bd.connect(host, user, password, db, port)

	return conn