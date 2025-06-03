from utils.tools import check_float_values

def define_non_recycable_trash() -> float:
    is_valid_input = False
    
    while not is_valid_input:
        try:
            non_recycable_trash_raw = input('\nQuantos kg de resíduos não recicláveis você gerou hoje?: ')

            non_recycable_trash = float(check_float_values(non_recycable_trash_raw))

        except TypeError:
            print('[ Valor inválido! Tente novamente. ]')
        
        except ValueError:
            print('[ Valor inválido! Tente novamente. ]')
        
        else:
            if non_recycable_trash < 0:
                print('[ Informe um valor maior ou igual a zero! Tente novamente. ]')
            else:
                is_valid_input = True
                return non_recycable_trash

def define_percentage_recycable() -> float:
    is_valid_input = False
    
    while not is_valid_input:
        try:
            recycable_raw = input('\nQual a porcentagem de resíduos reciclados no total (em %): ')

            recycable = float(check_float_values(recycable_raw))

        except TypeError:
            print('[ Valor inválido! Tente novamente. ]')
        
        except ValueError:
            print('[ Valor inválido! Tente novamente. ]')
        
        else:
            if recycable < 0 or recycable > 100:
                print('[ Valor inválido! Informe um número entre 0 e 100. Tente novamente. ]')
            else:
                is_valid_input = True
                return recycable
            
def define_non_recycable_trash_update(date) -> float:
    is_valid_input = False
    
    while not is_valid_input:
        try:
            non_recycable_trash_raw = input(f'\nQuantos kg de resíduos não recicláveis você gerou {date}?: ')

            non_recycable_trash = float(check_float_values(non_recycable_trash_raw))

        except TypeError:
            print('[ Valor inválido! Tente novamente. ]')
        
        except ValueError:
            print('[ Valor inválido! Tente novamente. ]')
        
        else:
            if non_recycable_trash < 0:
                print('[ Informe um valor maior ou igual a zero! Tente novamente. ]')
            else:
                is_valid_input = True
                return non_recycable_trash
            
def define_percentage_recycable_update(date) -> float:
    is_valid_input = False
    
    while not is_valid_input:
        try:
            recycable_raw = input(f'\nQual a porcentagem de resíduos reciclados no total dia {date} (em %): ')

            recycable = float(check_float_values(recycable_raw))

        except TypeError:
            print('[ Valor inválido! Tente novamente. ]')
        
        except ValueError:
            print('[ Valor inválido! Tente novamente. ]')
        
        else:
            if recycable < 0 or recycable > 100:
                print('[ Valor inválido! Informe um número entre 0 e 100. Tente novamente. ]')
            else:
                is_valid_input = True
                return recycable