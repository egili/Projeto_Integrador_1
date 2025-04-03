from datetime import date

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
        return 'Erro: Não existe dia ou mês negativo'
    elif year == 0 or year < -45:
        return 'Erro: Ano inválido'
    elif 5 <= day <= 14 and month == 10 and year == 1582:
        return 'Erro: Data inválida (transição do calendário Juliano para Gregoriano)'
    elif month > 12:
        return 'Erro: Mês inválido'
    elif (month == 4 or month == 6 or month == 9 or month == 1) and day > 30:
        return 'Erro: O mês informado tem apenas 30 dias'
    elif day > 31:
        return 'Erro: Dia inválido'
    elif isLeapYear(year) and month == 2 and day > 29:
        return 'Erro: Fevereiro em ano bissexto tem no máximo 29 dias'
    elif not isLeapYear(year) and month == 2 and day > 28:
        return 'Erro: Fevereiro em ano comum tem no máximo 28 dias'
    
    if day < 10:
        day = '0' + str(day)
    
    if month < 10:
        month = '0' + str(month)
    
    return f"{day}/{month}/{year}"


def which_date_use():
    while True:
        use_current_date = input('Quer preencher informações sobre a data de hoje? (S/N) ').upper()

        if use_current_date != 'N' and use_current_date != 'S':
            print("Opção inválida. Digite 'S' ou 'N'.")
            continue 
        
        if use_current_date == 'S':
            return format_current_date()

        is_day_valid   = False
        is_month_valid = False
        is_year_valid  = False

        while not is_day_valid or not is_month_valid or not is_year_valid:
            try:
                while not is_day_valid:
                    try:
                        day = int(input('Informe o dia '))
                    except ValueError:
                        print('Valor inválido para o dia, tente novamente')
                    else:
                        is_day_valid = True
                while not is_month_valid:
                    try:
                        month = int(input('Informe o mes '))
                    except ValueError:
                        print('Valor inválido para o mes, tente novamente')
                    else:
                        is_month_valid = True
                while not is_year_valid:
                    try:
                        year = int(input('Informe o ano '))
                    except ValueError:
                        print('Valor inválido para o ano, tente novamente')
                    else:
                        is_year_valid = True

            except ValueError:
                print('Erro: Digite apenas números para dia, mês e ano.')
                continue 

            formatted_date = format_given_date(day, month, year)

            if formatted_date.startswith('Erro'):
                print(formatted_date)
                is_day_valid   = False
                is_month_valid = False
                is_year_valid  = False 
            else:
                return formatted_date  
