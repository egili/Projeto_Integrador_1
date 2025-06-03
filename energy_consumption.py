from utils.tools import check_float_values

def define_energy_consumption() -> float:
    
    is_valid_input = False
    
    while not is_valid_input:
        try:
            energy_consumption_raw = input('\nQuantos kWh de energia você consumiu hoje?: ')

            energy_consumption = float(check_float_values(energy_consumption_raw))

        except TypeError:
            print('[ Valor inválido para o consumo de energia! Tente novamente. ]')
        
        except ValueError:
            print('[ Valor inválido para o consumo de energia! Tente novamente. ]')
        
        else:
            if energy_consumption < 0:
                print('[ Informe um valor maior ou igual a zero! Tente novamente. ]')
            else:
                is_valid_input = True
                return energy_consumption
            
def define_energy_consumption_update(date) -> float:
    
    is_valid_input = False
    
    while not is_valid_input:
        try:
            energy_consumption_raw = input(f'\nQuantos kWh de energia você consumiu no dia {date}?: ')

            energy_consumption = float(check_float_values(energy_consumption_raw))

        except TypeError:
            print('[ Valor inválido para o consumo de energia! Tente novamente. ]')
        
        except ValueError:
            print('[ Valor inválido para o consumo de energia! Tente novamente. ]')
        
        else:
            if energy_consumption < 0:
                print('[ Informe um valor maior ou igual a zero! Tente novamente. ]')
            else:
                is_valid_input = True
                return energy_consumption