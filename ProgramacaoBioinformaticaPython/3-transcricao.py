#Da bibliotexa Bio e o módulo Seq, importamos o Seq
from Bio.Seq import Seq

#seq que será o DNA imaginário
my_seq = Seq("ATG")

#sequencia de transcrição -> passagem de DNA para RNA
seq_rna = my_seq.transcribe()
print(seq_rna)

#sequencia de transcrição reversa -> de RNA para DNA
seq_dna = seq_rna.back_transcribe()
print(seq_dna)

