"""
Usaremos o BLAST local para alinhas duas sequencias que estão dentro desse diretório
antes de começar, deve saber qual versão do BLAST deve usar:
->blastn
->blastx
->blastp
->tblastm
OBS: olhar documento "importantBLAST.TXT"
"""
import subprocess
import os


"""
no exemplo, usaremos o blastp, mas deve saber qual é a query e o subject
-query: qual sequência será alinha
-subject: com qual sequência que vc irá alinhar
"""
subprocess.call(["blastp", "-query", "a.fasta", "-subject", "b.fasta"])


"""
podemos ainda exibir o resultado em formato tabular
o modo de exibição padrão é:
1.	 qseqid	 id do query (A sequência que estou comparando)
2.	 sseqid	 id do subject (a sequência a qual irei comparar)
3.	 pident	 porcentagem de matches
4.	 length	 tamanho do alinhamento
5.	 mismatch  número de mismatches
6.	 gapopen  número de gap openings
7.	 qstart	 onde começa o alinhamento da query
8.	 qend	 onde termina o alinhamento daquery
9.	 sstart	 onde começa o alinhamento do subject
10.	 send	 onde termina o alinhamento do subject
11.	 evalue	 valor estatístico (aleatoriedade)
12.	 bitscore  pontuação do alinhamento
"""
#o comando irá gerar um arquivo txt que armazenará o resultado tabular do alinhamento
os.system("blastp -query a.fasta -subject b.fasta -outfmt 6 > resultadoTabular.txt")

#fazendo a leitura do arquivo gerado com o resultado do alinhamento
print("\n\nFazendo a leitura do arquivo gerado")
linhas = open("resultadoTabular.txt").readlines()
for linha in linhas:
	print(linha)