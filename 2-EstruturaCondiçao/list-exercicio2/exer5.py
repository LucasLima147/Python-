from datetime import datetime
now = datetime.now()
ano = now.year


anoNascimento = int(input("Ano de Nascimento: "))
Idade = (now.year) - anoNascimento

if Idade >= 16:
    if Idade >= 18:
        print("->Você é maior de idade;\n->Já pode tirar a Carteira de Habilitação;\n->É OBRIGADO a votar.")
    else:
        print("->Você não é maior de idade;\n->PODE votar se quiser\n->Não pode tirar a Carteira de Habilitação.")
else:
    print("Você não é maior de idade e nem pode votar.")