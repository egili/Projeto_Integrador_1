from validators.sustentabilty_classification import define_water_sustentabilty_classification
from validators.sustentabilty_classification import define_energy_sustentabilty_classification
from validators.sustentabilty_classification import define_recycable_sustentabilty_classification
from validators.sustentabilty_classification import define_transportation_sustentability_classification
from utils.energy_consumption                import define_energy_consumption
from utils.water_consumption                 import define_water_consumption
from utils.trash_generation                  import define_non_recycable_trash, define_percentage_recycable
from utils.transportation                    import define_used_transport
from utils.define_date                       import which_date_use

def main():
    try_again = 'S'

    while try_again == 'S':
        try:
            user_defined_date = which_date_use()
            print(user_defined_date)
            
            water_consumption   = define_water_consumption()
            energy_consumption  = define_energy_consumption()
            non_recycable_trash = define_non_recycable_trash()
            valid_recycable     = define_percentage_recycable()
            used_transport      = define_used_transport()
            
            transportation_sustentability_classification = define_transportation_sustentability_classification(used_transport)
            recycable_sustentabilty_classification       = define_recycable_sustentabilty_classification(valid_recycable)
            energy_sustentabilty_classification          = define_energy_sustentabilty_classification(energy_consumption)
            water_sustentabilty_classification           = define_water_sustentabilty_classification(water_consumption)
            
            print(f'Para o dia {user_defined_date} a sustentabilidade é: ')
            print('')
            print(f'Consumo de água: {water_sustentabilty_classification}')
            print(f'Consumo de energia: {energy_sustentabilty_classification}')
            print(f'Geração de resíduos não reciclaveis: {recycable_sustentabilty_classification}')
            print(f'Uso de transporte: {transportation_sustentability_classification}')
            print('')
                    
        except ValueError:
            print('\nValores inválidos. Tente novamente')
        except KeyboardInterrupt:
            print('\nPrograma encerrado...')
            exit()
        else:
            is_valid_input = False
        while not is_valid_input:
            try:
                try_again = input('Quer informar outros dados de consumo? (S/N) ').upper()
            except ValueError:
                print('Opção inválida. Tente novamente')
            else:
                if try_again != 'S' and try_again != 'N':
                    print('Opção inválida. Tente novamente')
                else:
                    is_valid_input = True
                    if try_again == 'N':
                        print('\nFinalizando programa...')
                
main()