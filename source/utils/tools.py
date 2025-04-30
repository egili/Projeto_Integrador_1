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
