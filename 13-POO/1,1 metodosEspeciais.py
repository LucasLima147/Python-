class Livro():
    #__init__ usado como construtor ou executar determinada(s) operações na inicialização do objeto
    def __init__(self, titulo, autor, paginas):
        print("Livro criado")
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


    def __str__(self):
        return "Título: %s , autor: %s, páginas: %s" %(self.titulo, self.autor, self.paginas)

    def __len__(self):
        return self.paginas

    def len(self):
        print("Páginas do livro com o método comum ", self.paginas)

"""     MAIN    """
livro1 = Livro("Os lusíadas", "Luis de camões", 8816)

# com o método especial __str__ , ele irá retornar o que estiver dentro dele
print(livro1)
str(livro1)

print(len(livro1))
livro1.len()

""" REMOVENDO UM ATRIBUTO """
print(hasattr(livro1, "paginas"))
del livro1.paginas
print(hasattr(livro1, "paginas"))