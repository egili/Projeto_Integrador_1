from validators.sustentability_classification import define_water_sustentabilty_classification
from validators.sustentability_classification import define_energy_sustentabilty_classification
from validators.sustentability_classification import define_recycable_sustentabilty_classification
from validators.sustentability_classification import define_transportation_sustentability_classification
from utils.energy_consumption                 import define_energy_consumption
from utils.water_consumption                  import define_water_consumption
from utils.trash_generation                   import define_non_recycable_trash, define_percentage_recycable
from utils.transportation                     import define_used_transport
from utils.define_date                        import which_date_use
from utils.tools                              import clear_screen, press_enter_to_continue
from database.connection                      import conn, cursor
from database.create_tables                   import create_table_monitoring, create_table_monitoring_classifications
from database.insert_new_monitoring           import insert_monitoring                
from database.verify_monitoring_exists        import verify_if_exits
from database.select_monitoring               import select_all_monitoring

def main():
    create_table_monitoring()
    create_table_monitoring_classifications()

    try:
        while True:
            clear_screen()
            print("+------------------------------------------+")
            print("|               GreenTracker               |")
            print("+------------------------------------------+")
            print("| [1] Realizar um novo monitoramento       |")
            print("| [2] Visualizar monitoramentos anteriores |")
            print("| [3] Sair                                 |")
            print("+------------------------------------------+")
            user_choose = input("\n > ")
            

            if user_choose == "1":
                raw_date = which_date_use()

                splited_date = raw_date.split('/')
                date_for_db = f'{splited_date[2]}-{splited_date[1]}-{splited_date[0]}'

                if verify_if_exits(date_for_db):
                    clear_screen()

                    print('+----------------------------------------------------------+')
                    print(f'| Já existe um registro de monitoramento no dia {raw_date} |')
                    print('+----------------------------------------------------------+')

                    press_enter_to_continue()

                    continue

                user_defined_date = f'| Data registrada: {raw_date} |'

                clear_screen()

                print('+' + ('-' * (len(user_defined_date) - 2)) + '+')
                print(user_defined_date)
                print('+' + ('-' * (len(user_defined_date) - 2)) + '+')
                
                water_consumption   = define_water_consumption()
                energy_consumption  = define_energy_consumption()
                non_recycable_trash = define_non_recycable_trash()
                valid_recycable     = define_percentage_recycable()
                used_transport      = define_used_transport()
                
                transportation_sustentability_classification = define_transportation_sustentability_classification(used_transport)
                recycable_sustentabilty_classification       = define_recycable_sustentabilty_classification(valid_recycable)
                energy_sustentabilty_classification          = define_energy_sustentabilty_classification(energy_consumption)
                water_sustentabilty_classification           = define_water_sustentabilty_classification(water_consumption)
                
                press_enter_to_continue()
                clear_screen()

                biggest_word = len(recycable_sustentabilty_classification)

                if biggest_word > 0:
                    print('+' + ('-' * (41 + biggest_word)) + '+')
                    print(f'| Para o dia {raw_date} a sustentabilidade é:' + (' ' * ((41 + biggest_word) - (len(raw_date) + 35))) + ' |')
                    print('+' + ('-' * (41 + biggest_word)) + '+')
                    
                    print(f'| + Consumo de água: {water_sustentabilty_classification}', end='')
                    i = len(water_sustentabilty_classification) + 21
                    while i < (41 + biggest_word):
                        print(' ', end='')
                        i += 1
                    print(' |')
                    
                    print('|' + (' ' * (41 + biggest_word)) + '|')
                    
                    print(f'| + Consumo de energia: {energy_sustentabilty_classification}', end='')
                    i = len(energy_sustentabilty_classification) + 24
                    while i < (41 + biggest_word):
                        print(' ', end='')
                        i += 1
                    print(' |')
                    
                    print('|' + (' ' * (41 + biggest_word)) + '|')

                    print(f'| + Geração de resíduos não reciclaveis: {recycable_sustentabilty_classification} |')

                    print('|' + (' ' * (41 + biggest_word)) + '|')

                    print(f'| + Uso de transporte: {transportation_sustentability_classification}', end='')
                    i = len(transportation_sustentability_classification) + 23
                    while i < (41 + biggest_word):
                        print(' ', end='')
                        i += 1
                    print(' |')
                    print('+' + ('-' * (41 + biggest_word)) + '+')

                press_enter_to_continue()
                
                while True:
                    clear_screen()

                    print('+------------------------------------------------+')
                    print('| Deseja salvar o monitoramento realizado? (S/N) |')
                    print('+------------------------------------------------+')

                    store_in_db_choose = input('\n> ').upper()

                    if store_in_db_choose != 'N' and store_in_db_choose != 'S':
                        print('\n[ Opção inválida. Digite (S) ou (N). ]\n')

                        press_enter_to_continue()

                    elif store_in_db_choose == 'N':
                        clear_screen()

                        print('+---------------------------+')
                        print('| Monitoramento descartado! |')
                        print('+---------------------------+')

                        press_enter_to_continue()

                        break

                    else:
                        clear_screen()

                        if insert_monitoring(date_for_db, water_consumption, energy_consumption, non_recycable_trash, valid_recycable, used_transport, transportation_sustentability_classification, recycable_sustentabilty_classification, energy_sustentabilty_classification, water_sustentabilty_classification):
                            print('+----------------------------------+')
                            print('| Monitoramento salvo com sucesso! |')
                            print('+----------------------------------+')

                            press_enter_to_continue()
                        else:                            
                            press_enter_to_continue()

                        break

            elif user_choose == "2":
                clear_screen()

                monitoring_list = select_all_monitoring()

                if len(monitoring_list) > 0:

                    for item in monitoring_list:
                        number_list = [len(str(item[0])),len(str(item[1])),len(str(item[2])),len(str(item[3])),len(str(item[4])),len(str(item[5]))]
                        high_len = max(number_list)

                        print('+' + ('-' * (29 + high_len)) + '+')
                        print(f'| Data: {item[0]}', end="")
                        i = 0 
                        while i < ((29 + high_len) - 17):
                            print(' ', end="")
                            i+=1
                        print('|')
                        print(f'| Consumo de água: {item[1]}', end='') 
                        i = 0
                        while i < ((29 + high_len) - (18 + len(str(item[1])))):
                            print(' ', end="")
                            i+=1
                        print('|') 
                        print(f'| Consumo de energia: {item[2]}', end="")
                        i = 0
                        while i < ((29 + high_len) - (21 + len(str(item[2])))):
                            print(' ', end="")
                            i+=1
                        print('|') 
                        print(f'| Resíduos não reciclaveis: {item[3]}', end="")
                        i = 0
                        while i < (high_len - len(str(item[3]))):
                            print(' ', end="")
                            i+=1
                        print('  |')
                        print(f'| Resíduo reciclável: {item[4]}', end="")
                        i = 0
                        while i < ((29 + high_len) - (21 + len(str(item[4])))):
                            print(" ", end="")
                            i+=1
                        print('|')
                        print(f'| Uso de transporte: {item[5]}', end="")
                        i = 0
                        while i < ((29 + high_len) - (20 + len(str(item[5])))):
                            print(" ", end="")
                            i+=1
                        print('|')
                        print('+' + ('-' * (29 + high_len)) + '+\n')

                    print('\n+ Número de monitoramentos: ', len(monitoring_list))

                else:
                    print('[ Não existem monitoramentos no histórico! Realize um monitoramento e volte para essa opção mais tarde. ]')

                press_enter_to_continue()

            elif user_choose == "3":
                conn.close()
                cursor.close()
                
                clear_screen()

                break
            else:
                print("\n A opção digitada não existe! Escolha apenas entre os itens do menu.")
                press_enter_to_continue()
                
                continue
    
    except KeyboardInterrupt:
        clear_screen()
        print(" Finalizando o programa...")

        conn.close()
        cursor.close()

        exit()

main()
