import calendar
from datetime import date, timedelta
from statistics import median


def obter_semanas_do_proximo_mes():

    hoje = date.today()
    
    # CALCULANDO O PROXIMO MES
    if hoje.month == 12:  # SE ESTIVERMOS EM DEZEMBRO, O PROXIMO MES É JANEIRO DO PROXIMO ANO
        proximo_mes = 1
        ano = hoje.year + 1
    else:
        proximo_mes = hoje.month + 1
        ano = hoje.year

    # ORGANIZANDO OS DIAS POR SEMANA
    semanas = calendar.Calendar().monthdayscalendar(ano, proximo_mes)

    dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

    semanas_formatadas = []
    for semana in semanas:
        dias_formatados = []
        for i, dia in enumerate(semana):
            if dia != 0:  # DIAS FORA DO MES APARECEM COMO 0 NO monthdayscalendar
                if i != 5 and i != 6: # REMOVENDO "Sábado" e "Domingo" DO CALENDARIO
                    dias_formatados.append([dia, dias_semana[i]])

        semanas_formatadas.append(dias_formatados)

    return semanas_formatadas
