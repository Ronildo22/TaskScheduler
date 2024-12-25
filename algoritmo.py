from obter_semanas_do_proximo_mes import obter_semanas_do_proximo_mes


def agenda_mes(quant_task: int):

    semanas_do_proximo_mes = obter_semanas_do_proximo_mes()

    ativo = True    
    i_ultimo = -1

    while ativo:

        if quant_task != 0:
            
            # SE O INDICE CHEGAR NO MAXIMO POSSIVEL DA SEMANA 4 RESETAR PARA 0
            if i_ultimo == 4:
                i_ultimo = 0
            else:
                i_ultimo += 1

        else:
            ativo = False
        
        for semana in semanas_do_proximo_mes:
            
            if quant_task != 0:

                try:
                    
                    print(semana[i_ultimo])

                    quant_task -= 1

                except IndexError:
                    continue

            else:
                ativo = False

agenda_mes(100)
