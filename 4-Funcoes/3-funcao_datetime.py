""" 
O pacote 'datetime' é utilizado para pegar a data e hora atual, podendo ser útil nas aplicações
"""
import datetime                                         # importando o pacote

data_tempo_atual = datetime.datetime.now()              # pegando a data e hora de agora
print(data_tempo_atual)
''' pegando dados específicos da hora a partir do objeto acima'''
print(data_tempo_atual.hour)                            # pegando a hora de agora
print(data_tempo_atual.minute)                          # pegandp o minuto de agora
print(data_tempo_atual.second)                          # pegando o segundo de agora
print(data_tempo_atual.microsecond)                     # pegando o microsegundo de agora

print("..........................................")
''' pegando a data de hoje '''
hoje = datetime.date.today()                            # pegando a data atual
print(hoje)
''' pegand dados específicos da data a partir do objeto acima'''
print(hoje.ctime())                                     # dados completo da data atual
print(hoje.year)                                        # pegando o ano atual
print(hoje.month)                                       # pegando o mês atual (múmero)
print(hoje.day)                                         # pegando o dia atual

print("..........................................")
''' criando uma data, fazendo operações e também cálculos'''
criar_data = datetime.date(2015, 12, 14)                # .data(ano, mes, dia) -> Criando minha própria data
print(criar_data)
criar_data2 = criar_data.replace(year=2016, day=20)     # .replace(ano, mes, dia) -> trocar a data 
print(criar_data2)
print("Calculo datas:", criar_data2-criar_data)         # das operações básicas (+, -, *, /), só funcionou a subtração
