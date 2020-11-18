def tempoRegressivo(tempo):
	if tempo == 0:
		print("Feliz Ano Novo")
	else:
		print(tempo)
		tempoRegressivo(tempo-1)

tempoRegressivo(993)