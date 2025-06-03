import os

def clear_screen():
    if os.name != 'posix':
        os.system('cls')
    else:
        os.system('clear')

def press_enter_to_continue():
    input("\n\nPressione ENTER para continuar...")

def check_float_values(value_raw: str):
    number_of_comma = 0
    for i in value_raw:
        if i == ',':
            number_of_comma += 1

    if number_of_comma >= 2:
        return None

    value = value_raw.replace(',', '.')

    return value

def format_date(raw_date):
    splited_date = raw_date.split('/')
    
    return f'{splited_date[2]}-{splited_date[1]}-{splited_date[0]}'

def style_for_monitoring(monitoring_list, classification_list):
    index = 0
    for item in monitoring_list:
        number_list_monitoring = [len(str(item[0])),len(str(item[1])),len(str(item[2])),len(str(item[3])),len(str(item[4])),len(str(item[5]))]
        number_list_classifications = [len(str(classification_list[index][0][1])), len(str(classification_list[index][0][2])), len(str(classification_list[index][0][3])), len(str(classification_list[index][0][4]))]
        high_len = 0

        if max(number_list_classifications) > max(number_list_monitoring):
            high_len = max(number_list_classifications)
        else:
            high_len = max(number_list_monitoring)

        print('+' + ('-' * (41 + high_len)) + '+')
        print(f'| Data: {item[0].strftime("%d/%m/%Y")}', end="")
        i = 0
        if len(item[0].strftime("%d/%m/%Y")) < 10:
            i = len(item[0].strftime("%d/%m/%Y")) - 10
        while i < ((41 + high_len) - 17):
            print(' ', end="")
            i+=1
        print('|')
        print('|' + ('-' * (41 + high_len)) + '|')
        print(f'| + Consumo de água: {item[1]}', end='') 
        i = 2
        while i < ((41 + high_len) - (18 + len(str(item[1])))):
            print(' ', end="")
            i+=1
        print('|') 
        print(f'| + Consumo de energia: {item[2]}', end="")
        i = 2
        while i < ((41 + high_len) - (21 + len(str(item[2])))):
            print(' ', end="")
            i+=1
        print('|') 
        print(f'| + Resíduos não reciclaveis: {item[3]}', end="")
        i = 1
        while i < ((34 - 23) + high_len - len(str(item[3]))):
            print(' ', end="")
            i+=1
        print('  |')
        print(f'| + Resíduo reciclável: {item[4]}', end="")
        i = 2
        while i < ((41 + high_len) - (21 + len(str(item[4])))):
            print(" ", end="")
            i+=1
        print('|')
        print(f'| + Uso de transporte: {item[5]}', end="")
        i = 2
        while i < ((41 + high_len) - (20 + len(str(item[5])))):
            print(" ", end="")
            i+=1
        print('|')
        print('+' + ('-' * (41 + high_len)) + '+')
        print(f"| + Consumo de água: {classification_list[index][0][1]}", end="")
        i = 0
        while i < ((41 + high_len) - (20 + len(str(classification_list[index][0][1])))):
            print(" ", end="")
            i += 1
        print("|")
        print(f"| + Consumo de energia: {classification_list[index][0][2]}", end="")
        i = 0
        while i < ((41 + high_len) - (23 + len(str(classification_list[index][0][2])))):
            print(" ", end="")
            i += 1
        print("|")
        print(f"| + Geração de resíduos não reciclaveis: {classification_list[index][0][3]} |")
        print(f"| + Uso de transporte: {classification_list[index][0][4]}", end="")
        i = 0
        while i < ((41 + high_len) - (22 + len(str(classification_list[index][0][4])))):
            print(" ", end="")
            i += 1
        print("|")
        print('+' + ('-' * (41 + high_len)) + '+')

        index += 1