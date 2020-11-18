teste = "m@al s@abe que eu Am0o vçc"
for letra in teste:
    if letra == "@" or letra == "0" or letra == "ç":
        if letra == "@":
            teste = teste.replace(letra, "")

print(teste)