def define_non_recycable_trash() -> float:
    
    is_valid_input = False
    
    while not is_valid_input:
        try:
            non_recycable_trash = float(input('\nQuantos kg de resíduos não recicláveis você gerou hoje?: '))
        except ValueError:
            print('Valor invalido.')
        else:
            if non_recycable_trash < 0:
                print('Valor inválido. Informe um número maior que zero.')
            else:
                is_valid_input = True
                return non_recycable_trash

def define_percentage_recycable() -> float:
    
    is_valid_input = False
    
    while not is_valid_input:
        try:
            recycable = float(input('\nQual a porcentagem de resíduos reciclados no total (em %): '))
        except ValueError:
            print('Valor invalido')
        else:
            if recycable < 0 or recycable > 100:
                print('Valor inválido. Informe um numero entre 0 e 100.')
            else:
                is_valid_input = True
                return recycable
