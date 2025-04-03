
def define_energy_consumption() -> float:
    
    is_valid_input = False
    
    while not is_valid_input:
        try:
            energy_consumption = float(input('\nQuantos kWh de energia você consumiu hoje?: '))
        except ValueError:
            print('Informa um valor válido para o consumo de energia')
        else:
            if energy_consumption < 0:
                print('Informe um valor maior ou igual a zero')
            else:
                is_valid_input = True
                return energy_consumption
    
