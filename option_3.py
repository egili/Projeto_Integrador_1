from database.select_monitoring               import select_monitoring_dates, select_specif_monitoring
from database.update_tables                   import update_monitoring_table
from utils.tools                              import clear_screen, press_enter_to_continue, style_for_monitoring, format_date
from utils.define_date                        import which_date_use_for_update
from utils.energy_consumption                 import define_energy_consumption_update
from utils.water_consumption                  import define_water_consumption_update
from utils.trash_generation                   import define_non_recycable_trash_update, define_percentage_recycable_update
from utils.transportation                     import define_used_transport_update
from validators.sustentability_classification import define_energy_sustentabilty_classification, define_recycable_sustentabilty_classification, define_transportation_sustentability_classification, define_water_sustentabilty_classification

def update_option():
    dates_for_update = select_monitoring_dates()

    update_monitoring = 0

    while update_monitoring == 0:
        if len(dates_for_update) > 0:
            clear_screen()

            print("+----------------------------------+")
            print("| Datas disponíveis para edição:   |")
            print("+----------------------------------+")
            print("|                                  |")
            for date in dates_for_update:
                if len(date[0].strftime('%d/%m/%Y')) < 10:
                    print(f"|          * {date[0].strftime('%d/%m/%Y')} *          " + (" " * (10 - len(date[0].strftime('%d/%m/%Y')))) + "|")
                else:
                    print(f"|          * {date[0].strftime('%d/%m/%Y')} *          |")
                print("|                                  |")
                print("+----------------------------------+")

            raw_update_date = which_date_use_for_update()

            update_choose = format_date(raw_update_date)

            update_monitoring_result = select_specif_monitoring(update_choose)

            while True:
                clear_screen()

                if len(update_monitoring_result[0]) > 0:
                    style_for_monitoring(update_monitoring_result[0], update_monitoring_result[1])

                    print("[ Você tem certeza que deseja editar esse monitoramento? (S/N) ]")

                    confirmation_update = input("\n> ").upper()
                    
                    if confirmation_update != 'N' and confirmation_update != 'S':
                        print('\n[ Opção inválida. Digite (S) ou (N). ]\n')

                        press_enter_to_continue()

                        continue

                    elif confirmation_update == 'N':
                        clear_screen()

                        print("+---------------------+")
                        print("| Operação cancelada! |")
                        print("+---------------------+")

                        update_monitoring = 1

                        press_enter_to_continue()

                        break

                    else:
                        clear_screen()

                        water_consumption_update   = define_water_consumption_update(raw_update_date)
                        energy_consumption_update  = define_energy_consumption_update(raw_update_date)
                        non_recycable_trash_update = define_non_recycable_trash_update(raw_update_date)
                        valid_recycable_update     = define_percentage_recycable_update(raw_update_date)
                        used_transport_update      = define_used_transport_update(raw_update_date)

                        transportation_sustentability_classification_update = define_transportation_sustentability_classification(used_transport_update)
                        recycable_sustentabilty_classification_update       = define_recycable_sustentabilty_classification(valid_recycable_update)
                        energy_sustentabilty_classification_update          = define_energy_sustentabilty_classification(energy_consumption_update)
                        water_sustentabilty_classification_update           = define_water_sustentabilty_classification(water_consumption_update)

                        if update_monitoring_table(update_choose, water_consumption_update, energy_consumption_update, non_recycable_trash_update, valid_recycable_update, used_transport_update, transportation_sustentability_classification_update, recycable_sustentabilty_classification_update, energy_sustentabilty_classification_update, water_sustentabilty_classification_update):
                            update_result = select_specif_monitoring(update_choose)

                            clear_screen()

                            style_for_monitoring(update_result[0], update_result[1])

                            print('\n[ Edição concluída com sucesso! ]')

                            press_enter_to_continue()

                            update_monitoring = 1

                            break

                        else:
                            clear_screen()

                            print('[ Houve um erro ao editar o monitoramento! Tente novamente mais tarde. ]')

                            press_enter_to_continue()

                            update_monitoring = 1

                            break
                else:
                    print("+---------------------------------------------" + ("-" * len(raw_update_date)) + "+")
                    print(f"| Não existe nenhum monitoramento com a data {raw_update_date} |")
                    print("+---------------------------------------------" + ("-" * len(raw_update_date)) + "+")

                    update_monitoring = 1

                    press_enter_to_continue()

                    break

        else:
            clear_screen()

            print("[ Não existem monitoramentos no histórico! Realize um monitoramento e volte para essa opção mais tarde. ]")

            update_monitoring = 1

            press_enter_to_continue()