from validators.sustentability_classification import define_water_sustentabilty_classification
from validators.sustentability_classification import define_energy_sustentabilty_classification
from validators.sustentability_classification import define_recycable_sustentabilty_classification
from validators.sustentability_classification import define_transportation_sustentability_classification
from utils.energy_consumption                 import define_energy_consumption
from utils.water_consumption                  import define_water_consumption
from utils.trash_generation                   import define_non_recycable_trash, define_percentage_recycable
from utils.transportation                     import define_used_transport
from utils.define_date                        import which_date_use, which_date_use_for_exclusion
from utils.tools                              import clear_screen, press_enter_to_continue, format_date, style_for_monitoring
from database.connection                      import conn, cursor
from database.create_tables                   import create_table_monitoring, create_table_monitoring_classifications
from database.insert_new_monitoring           import insert_monitoring                
from database.verify_monitoring_exists        import verify_if_exits
from database.select_monitoring               import select_all_monitoring, select_monitoring_dates, select_specif_monitoring
from database.delete_monitoring               import delete_from_db
from menu.option_3                            import update_option

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
            print("| [3] Editar um monitoramento              |")
            print("| [4] Excluir um monitoramento             |")
            print("| [5] Sair                                 |")
            print("+------------------------------------------+")
            user_choose = input("\n > ")
            

            if user_choose == "1":
                raw_date = which_date_use()

                date_for_db = format_date(raw_date)

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
                        while True:
                            clear_screen()

                            print('+---------------------------------------------------------+')
                            print('| Tem certeza que deseja descartar o monitoramento? (S/N) |')
                            print('|                                                         |')
                            print('| * CASO VOCÊ CONFIRME, O MONITORAMENTO SEJA DESCARTADO * |')
                            print('+---------------------------------------------------------+')

                            discard_confirm = input('\n> ').upper()

                            if discard_confirm != 'N' and discard_confirm != 'S':
                                print('\n[ Opção inválida. Digite (S) ou (N). ]\n')

                                press_enter_to_continue()

                                continue
                            
                            elif discard_confirm == 'S':

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

                    break

            elif user_choose == "2":
                clear_screen()

                monitoring_list = select_all_monitoring()

                if len(monitoring_list[0]) > 0:

                    style_for_monitoring(monitoring_list[0], monitoring_list[1])

                    print('\n+ Número de monitoramentos: ', len(monitoring_list[0]))

                else:
                    print('[ Não existem monitoramentos no histórico! Realize um monitoramento e volte para essa opção mais tarde. ]')

                press_enter_to_continue()

            elif user_choose == "3":
                update_option()

            elif user_choose == "4":
                dates_for_exlusion = select_monitoring_dates()

                monitoring_exclusion = 0
                while monitoring_exclusion == 0:
                    clear_screen()

                    if len(dates_for_exlusion) > 0:

                        print("+----------------------------------+")
                        print("| Datas disponíveis para exclusão: |")
                        print("+----------------------------------+")
                        print("|                                  |")

                        for date in dates_for_exlusion:
                            if len(date[0].strftime('%d/%m/%Y')) < 10:
                                print(f"|          * {date[0].strftime('%d/%m/%Y')} *          " + (" " * (10 - len(date[0].strftime('%d/%m/%Y')))) + "|")
                            else:
                                print(f"|          * {date[0].strftime('%d/%m/%Y')} *          |")
                            print("|                                  |")
                        print("+----------------------------------+")

                        raw_exclusion_date = which_date_use_for_exclusion()

                        exclusion_choose = format_date(raw_exclusion_date)

                        exclusion_monitoring_result = select_specif_monitoring(exclusion_choose)

                        clear_screen()

                        if len(exclusion_monitoring_result[0]) > 0:
                            while True:
                                clear_screen()

                                style_for_monitoring(exclusion_monitoring_result[0], exclusion_monitoring_result[1])

                                print("[ Você tem certeza que deseja excluir esse monitoramento? (S/N) ]")

                                confirmation_exclude = input("\n> ").upper()
                                
                                if confirmation_exclude != 'N' and confirmation_exclude != 'S':
                                    print('\n[ Opção inválida. Digite (S) ou (N). ]\n')

                                    press_enter_to_continue()

                                    continue

                                elif confirmation_exclude == 'N':
                                    clear_screen()

                                    print("+---------------------+")
                                    print("| Operação cancelada! |")
                                    print("+---------------------+")

                                    press_enter_to_continue()

                                    monitoring_exclusion = 1

                                    break

                                else:
                                    delete_from_db(exclusion_choose)

                                    clear_screen()

                                    print("+-------------------------------------+")
                                    print("| Monitoramento deletado com sucesso! |")
                                    print("+-------------------------------------+")

                                    press_enter_to_continue()

                                    monitoring_exclusion = 1

                                    break
                        else:
                            clear_screen()
                            
                            print("+---------------------------------------------" + ("-" * len(raw_exclusion_date)) + "+")
                            print(f"| Não existe nenhum monitoramento com a data {raw_exclusion_date} |")
                            print("+---------------------------------------------" + ("-" * len(raw_exclusion_date)) + "+")

                            press_enter_to_continue()

                    else:
                        print("[ Não existem monitoramentos no histórico! Realize um monitoramento e volte para essa opção mais tarde. ]")

                        press_enter_to_continue()

                        monitoring_exclusion = 1

            elif user_choose == "5":
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
