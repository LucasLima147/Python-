class Socio:
    # construtor da classe, sendo que cada vez que eu criar uma instância, ele será executado
    # cada uma dessas variáveis são um atributo da classe que será inicializado em cada instância
    """ ---> O uso da palabra 'self' é obrigatório nos construtores e nos métodos"""
    def __init__(self):
        self.nome = ""
        self.cpf = ""
        self.rg = ""
        self.nascimento = ""
        self.telefone = ""
        self.endereco = ""
    
    # as funções dentro de cada classe são os métodos
    def cadastrar(self, nome, cpf, rg, nascimento, telefone, endereco):
        # usamos a palabra reservada "self" quadno queremos referir a um atributo/método dentro da própria classe
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.nascimento = nascimento
        self.telefone = telefone
        self.endereco = endereco
    
    def exibirCadastro(self):
        print(" Nome: {0}\n CPF: {1}\n RG: {2}\n Data de Nascimento: {3}\n Telefone: {4}\n Endereço: {5}".format(self.nome, self.cpf, self.rg, self.nascimento, self.telefone, self.endereco))


# instanciando uma classe
novoSocio = Socio()
# aqui vemos que temos nossa instância ou objeto
print(novoSocio)
# acessando o valor de um atributo
print(type(novoSocio.rg))
# usando os método da classe
novoSocio.cadastrar("Lucas", "000.111.222-33", "00.111.222", "01/01/0001", "(00) 99999-9999", "Rua teste")
novoSocio.exibirCadastro()
print()
###########################################################################

class Pessoa():
    def __init__(self, nome, nascimento, telefone):
        self.nome = nome
        self.nascimento = nascimento
        self.telefone = telefone
    
    def exibirCadastro(self):
        print(" Nome: {0}\n Data de Nascimento: {1}\n Telefone: {2}".format(self.nome, self.nascimento, self.telefone))

# demonstrando uma instanciar um objeto, usabdo o construtor com parâmetros
novaPessoa = Pessoa("Livia","01/01/0001", "(00) 99999-9999")
#podemos verificar se determinado atributo existe em uma classe
if hasattr(novaPessoa, "cpf"): print("Existe")
else: setattr(novaPessoa, "cpf", "111.222.333-44")

novaPessoa.exibirCadastro()

####################################################################
""" uso de método de uma classe """
class Circulo:
    pi = 3.14

    #Quando for criada uma nova instância da classe, o construtor será executado
    # raio = 5 --> por default raio se inicializara com 5 se não for passado nenhum valor
    def __init__(self, raio = 5):
        self.raio = raio

    #Método para calcular a área
    def area(self):
        return (self.raio * self.raio) * Circulo.pi

    #SETTER & GETTER
    def setRaio(self, newRaio):
        self.raio = newRaio

    def getRaio(self):
        return self.raio


circ = Circulo()
print(circ.getRaio(), circ.area())

circ.setRaio(8)
print(circ.getRaio(), circ.area())