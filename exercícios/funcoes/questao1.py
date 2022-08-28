def formata_hora(hora):
   return leading_zero(hora[0]).format() + ':' + leading_zero(hora[1]) + ':' + leading_zero(hora[2])

def leading_zero(valor):
    return "{:02d}".format(valor)

def soma_horas (hora_inicio, acrescimo):
    
    segundo = hora_inicio[2] + acrescimo[2]
    minuto = hora_inicio[1] + acrescimo[1]
    hora = hora_inicio[0] + acrescimo[0]

    if segundo > 59:
        minuto += 1
        segundo = segundo - 60

    if minuto > 59:
        hora += 1
        minuto = minuto - 60

    if hora > 23:
        hora = hora - 24

    hora_final = [hora, minuto, segundo]
    
    return hora_final


ronda1 = [1,0,0]
ronda2 = [2,10,30]
ronda3 = [4,40,50]
ronda4 = [12,5,5]

hora_inicio = [0,0,0]
hora_inicio[0] = int(input())
hora_inicio[1] = int(input())
hora_inicio[2] = int(input())

hora_final = hora_inicio
print(formata_hora(hora_final))
hora_final = soma_horas(hora_inicio, ronda1)
print(formata_hora(hora_final))
hora_final = soma_horas(hora_inicio, ronda2)
print(formata_hora(hora_final))
hora_final = soma_horas(hora_inicio, ronda3)
print(formata_hora(hora_final))
hora_final = soma_horas(hora_inicio, ronda4)
print(formata_hora(hora_final))



