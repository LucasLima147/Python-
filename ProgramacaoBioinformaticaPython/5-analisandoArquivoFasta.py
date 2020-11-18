#SeqIO é a classe que analisa arquivos de sequencias
from Bio import SeqIO

'''
Laço de repetição:
	->usado para pegar cada sequencia do meu arquivo fasta
SeqIO.parse("arquivo.fasta")
	->método que faz a análise do arquivo FASTA
	->retorna cada linha das sequências e os títulos
'''
for fasta in SeqIO.parse("5-my_seq.fasta", "fasta"):

	#fasta.id -> Pega os IDs(títulos das sequencias)
	print(fasta.id)
	
	#fasta.seq -> pega as sequencias
	print(fasta.seq)

