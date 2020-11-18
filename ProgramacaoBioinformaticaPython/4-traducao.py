#Da bibliotexa Bio e o módulo Seq, importamos o Seq
from Bio.Seq import Seq

#seq que será o DNA imaginário
my_seq = Seq("ATG")
print(my_seq, "| minha sequencia")

#sequencia de transcrição -> passagem de DNA para RNA
seq_rna = my_seq.transcribe()
print(seq_rna, "| minha sequencia transcrita (RNA)")

#sequencia de tradução ->passagem de RNA para molde/sequencia de aminoácios
seq_trad = seq_rna.translate()
print(seq_trad, "| minha sequencia traduzidas do RNA(sequencia de aminoacios para forma a proteina")

#posso aplicar isso para o DNA também
seq_dna = seq_rna.back_transcribe()
seq_trad = seq_dna.translate()
print(seq_trad, "| minha sequencia traduzidas do DNA(sequencia de aminoacios para forma a proteina")