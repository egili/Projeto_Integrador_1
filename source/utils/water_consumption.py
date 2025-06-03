from utils.tools import check_float_values

def define_water_consumption() -> float:
    
    is_valid_input = False
    
    while not is_valid_input:
        try:
            water_consumption_raw = input('\nQuantos litros de água você consumiu hoje? (Aprox. em litros): ')
            
            water_consumption = float(check_float_values(water_consumption_raw))

        except TypeError:
            print('[ Valor inválido para o consumo de água! Tente novamente. ]')

        except ValueError:
            print('[ Valor inválido para o consumo de água! Tente novamente. ]')
       
        else:
            if water_consumption < 0:
                print('[ Informe um valor maior ou igual a zero! Tente novamente. ]')
            else:
                is_valid_input = True
                return water_consumption
            
def define_water_consumption_update(date) -> float:
    
    is_valid_input = False
    
    while not is_valid_input:
        try:
            water_consumption_raw = input(f'\nQuantos litros de água você consumiu no dia {date}? (Aprox. em litros): ')
            
            water_consumption = float(check_float_values(water_consumption_raw))

        except TypeError:
            print('[ Valor inválido para o consumo de água! Tente novamente. ]')

        except ValueError:
            print('[ Valor inválido para o consumo de água! Tente novamente. ]')
       
        else:
            if water_consumption < 0:
                print('[ Informe um valor maior ou igual a zero! Tente novamente. ]')
            else:
                is_valid_input = True
                return water_consumption