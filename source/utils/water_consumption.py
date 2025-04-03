
def define_water_consumption() -> float:
    
    is_valid_input = False
    
    while not is_valid_input:
        try:
            water_consumption = float(input('\nQuantos litros de água você consumiu hoje? (Aprox. em litros): '))
        except ValueError:
            print('Informa um valor válido para o consumo de água')
        else:
            if water_consumption < 0:
                print('Informe um valor maior ou igual a zero')
            else:
                is_valid_input = True
                return water_consumption
    
