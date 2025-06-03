from datetime    import date
from utils.tools import press_enter_to_continue, clear_screen

def isLeapYear(year):
    if year < 1583 and year % 4 == 0:
        return True
    elif year > 1583 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    elif year % 400 == 0:
        return True
    return False 

def format_current_date():
    return date.today().strftime("%d/%m/%Y")

def format_given_date(day: int, month: int, year: int) -> str:
    if day < 0 or month < 0:
        return 'Erro: Não existe dia ou mês negativo! Tente novamente.'
    elif year == 0 or year < -45:
        return 'Erro: Ano inválido! Tente novamente.'
    elif 5 <= day <= 14 and month == 10 and year == 1582:
        return 'Erro: Data inválida (transição do calendário Juliano para Gregoriano)! Tente novamente.'
    elif month > 12:
        return 'Erro: Mês inválido'
    elif (month == 4 or month == 6 or month == 9 or month == 1) and day > 30:
        return 'Erro: O mês informado tem apenas 30 dias! Tente novamente.'
    elif day > 31:
        return 'Erro: Dia inválido'
    elif isLeapYear(year) and month == 2 and day > 29:
        return 'Erro: Fevereiro em ano bissexto tem no máximo 29 dias! Tente novamente.'
    elif not isLeapYear(year) and month == 2 and day > 28:
        return 'Erro: Fevereiro em ano comum tem no máximo 28 dias! Tente novamente.'
    
    if day < 10:
        day = '0' + str(day)
    
    if month < 10:
        month = '0' + str(month)
    
    return f"{day}/{month}/{year}"


def which_date_use():
    while True:
        clear_screen()

        print('+----------------------------------+')
        print('| Deseja preencher as informações  |\n| referentes à data de hoje? (S/N) |')
        print('+----------------------------------+')

        use_current_date = input('\n> ').upper()

        if use_current_date != 'N' and use_current_date != 'S':
            print("\n[ Opção inválida. Digite (S) ou (N). ]\n")
            press_enter_to_continue()

            continue
        
        if use_current_date == 'S':
            return format_current_date()

        is_day_valid   = False
        is_month_valid = False
        is_year_valid  = False

        while not is_day_valid or not is_month_valid or not is_year_valid:
            try:
                clear_screen()

                print('+----------------+')
                print('| Informe a data |')
                print('+----------------+\n')
                while not is_day_valid:
                    try:
                        day = int(input('+ Dia: '))
                    except ValueError:
                        print('[ Erro: Valor inválido para o dia! Tente novamente. ]\n')
                    else:
                        if day > 0 and day < 32:
                            is_day_valid = True
                        elif day > 31:
                            print('[ Erro: Valor inválido para o dia! Um mês possuí até 31 dias. Tente novamente. ]\n')
                            continue
                        else:
                            print('[ Erro: Valor inválido para o dia! Tente novamente. ]\n')
                            continue
                while not is_month_valid:
                    try:
                        month = int(input('+ Mês: '))
                    except ValueError:
                        print('[ Erro: Valor inválido para o mês! Tente novamente. ]\n')
                    else:
                        if month > 0 and month <= 12:
                            is_month_valid = True
                        elif month > 12:
                            print('[ Erro: Valor inválido para o mês! Um ano possuí até 12 meses. Tente novamente. ]\n')
                            continue
                        else:
                            print('[ Erro: Valor inválido para o mês! Tente novamente. ]\n')
                            continue
                while not is_year_valid:
                    try:
                        year = int(input('+ Ano: '))
                    except ValueError:
                        print('[ Erro: Valor inválido para o ano! Tente novamente. ]\n')
                    else:
                        if year > 0 and year <= 9999:
                            is_year_valid = True
                        elif year > 9999:
                            print('[ Erro: Valor inválido para o ano! Tente novamente. ]\n')
                        else:
                            print('[ Erro: Valor inválido para o ano! Tente novamente. ]\n')
                            continue

            except ValueError:
                print('Erro: Digite apenas números para dia, mês e ano.')
                press_enter_to_continue()

                continue 

            formatted_date = format_given_date(day, month, year)

            if formatted_date.startswith('Erro'):
                print(f'[ {formatted_date} ]')
                press_enter_to_continue()
                is_day_valid   = False
                is_month_valid = False
                is_year_valid  = False 
            else:
                return formatted_date  


def which_date_use_for_update():
    while True:
        is_day_valid   = False
        is_month_valid = False
        is_year_valid  = False

        while not is_day_valid or not is_month_valid or not is_year_valid:
            try:
                print('[ Insira uma data para a editar. ]\n')

                while not is_day_valid:
                    try:
                        day = int(input('+ Dia: '))
                    except ValueError:
                        print('[ Erro: Valor inválido para o dia! Tente novamente. ]\n')
                    else:
                        if day > 0 and day < 32:
                            is_day_valid = True
                        elif day > 31:
                            print('[ Erro: Valor inválido para o dia! Um mês possuí até 31 dias. Tente novamente. ]\n')
                            continue
                        else:
                            print('[ Erro: Valor inválido para o dia! Tente novamente. ]\n')
                            continue
                while not is_month_valid:
                    try:
                        month = int(input('+ Mês: '))
                    except ValueError:
                        print('[ Erro: Valor inválido para o mês! Tente novamente. ]\n')
                    else:
                        if month > 0 and month <= 12:
                            is_month_valid = True
                        elif month > 12:
                            print('[ Erro: Valor inválido para o mês! Um ano possuí até 12 meses. Tente novamente. ]\n')
                            continue
                        else:
                            print('[ Erro: Valor inválido para o mês! Tente novamente. ]\n')
                            continue
                while not is_year_valid:
                    try:
                        year = int(input('+ Ano: '))
                    except ValueError:
                        print('[ Erro: Valor inválido para o ano! Tente novamente. ]\n')
                    else:
                        if year > 0 and year <= 9999:
                            is_year_valid = True
                        elif year > 9999:
                            print('[ Erro: Valor inválido para o ano! Tente novamente. ]\n')
                        else:
                            print('[ Erro: Valor inválido para o ano! Tente novamente. ]\n')
                            continue

            except ValueError:
                print('Erro: Digite apenas números para dia, mês e ano.')
                press_enter_to_continue()

                continue 

            formatted_date = format_given_date(day, month, year)

            if formatted_date.startswith('Erro'):
                print(f'[ {formatted_date} ]')
                press_enter_to_continue()
                is_day_valid   = False
                is_month_valid = False
                is_year_valid  = False 
            else:
                return formatted_date  

def which_date_use_for_exclusion():
    while True:
        is_day_valid   = False
        is_month_valid = False
        is_year_valid  = False

        while not is_day_valid or not is_month_valid or not is_year_valid:
            try:
                print('[ Insira uma data para a exlcusão. ]\n')

                while not is_day_valid:
                    try:
                        day = int(input('+ Dia: '))
                    except ValueError:
                        print('[ Erro: Valor inválido para o dia! Tente novamente. ]\n')
                    else:
                        if day > 0 and day < 32:
                            is_day_valid = True
                        elif day > 31:
                            print('[ Erro: Valor inválido para o dia! Um mês possuí até 31 dias. Tente novamente. ]\n')
                            continue
                        else:
                            print('[ Erro: Valor inválido para o dia! Tente novamente. ]\n')
                            continue
                while not is_month_valid:
                    try:
                        month = int(input('+ Mês: '))
                    except ValueError:
                        print('[ Erro: Valor inválido para o mês! Tente novamente. ]\n')
                    else:
                        if month > 0 and month <= 12:
                            is_month_valid = True
                        elif month > 12:
                            print('[ Erro: Valor inválido para o mês! Um ano possuí até 12 meses. Tente novamente. ]\n')
                            continue
                        else:
                            print('[ Erro: Valor inválido para o mês! Tente novamente. ]\n')
                            continue
                while not is_year_valid:
                    try:
                        year = int(input('+ Ano: '))
                    except ValueError:
                        print('[ Erro: Valor inválido para o ano! Tente novamente. ]\n')
                    else:
                        if year > 0 and year <= 9999:
                            is_year_valid = True
                        elif year > 9999:
                            print('[ Erro: Valor inválido para o ano! Tente novamente. ]\n')
                        else:
                            print('[ Erro: Valor inválido para o ano! Tente novamente. ]\n')
                            continue

            except ValueError:
                print('Erro: Digite apenas números para dia, mês e ano.')
                press_enter_to_continue()

                continue 

            formatted_date = format_given_date(day, month, year)

            if formatted_date.startswith('Erro'):
                print(f'[ {formatted_date} ]')
                press_enter_to_continue()
                is_day_valid   = False
                is_month_valid = False
                is_year_valid  = False 
            else:
                return formatted_date  