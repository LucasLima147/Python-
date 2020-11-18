#Da bibliotexa Bio e o módulo Seq, importamos o Seq
from Bio.Seq import Seq


my_seq = Seq("ATG")
print(my_seq, "minha sequencia")

#sequencia Complementar
seq_comp = my_seq.complement()
print(seq_comp, "sequencia Complementar")

#sequencia reversa complementar
seq_rever_comp = my_seq.reverse_complement()
print(seq_rever_comp, "sequencia reversa complementar")