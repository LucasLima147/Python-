# Inicio do evento
diaInicio = input().split()
del diaInicio[0]
diaInicio = int(diaInicio[0])
horarioInicio = input().split()
del horarioInicio[1]
del horarioInicio[2]

# Fim do evento
diaFinal = input().split()
del diaFinal[0]
diaFinal = int(diaFinal[0])
horarioFinal = input().split()
del horarioFinal[1]
del horarioFinal[2]

# PREPRARO DAS VÁRIAVEIS
dias = horas = minutos = segundos = 0
# >>> SEGUNDOS
if int(horarioFinal[2]) <= int(horarioInicio[2]):
    segundos = (60 - int(horarioInicio[2])) + int(horarioFinal[2])
    if segundos < 60:
        minutos -= 1
    else:
        segundos -= 60
else: 
    segundos = int(horarioFinal[2]) - int(horarioInicio[2])
# >>> MINUTOS
if int(horarioFinal[1]) <= int(horarioInicio[1]):
    minutos = ((60 - int(horarioInicio[1])) + int(horarioFinal[1])) + minutos
    if minutos < 60:
        horas = -1
    else:
        minutos -= 60
        
else:
    minutos = int(horarioFinal[1]) - int(horarioInicio[1]) + minutos

# >>> horas
if int(horarioFinal[0]) <= int(horarioInicio[0]):
    horas = ((24 - int(horarioInicio[0])) + int(horarioFinal[0])) + horas
    if horas < 24:
        dias -= 1
    else:
        horas -= 24
        
else:
    horas = int(horarioFinal[0]) - int(horarioInicio[0]) + horas
    print("aqui Horas")
dias += diaFinal - diaInicio

print("{0} dia(s)\n{1} hora(s)\n{2} minuto(s)\n{3} segundo(s)".format(dias, horas, minutos, segundos))