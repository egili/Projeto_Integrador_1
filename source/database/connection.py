import mysql.connector
import os
from dotenv      import load_dotenv
from utils.tools import clear_screen, press_enter_to_continue

load_dotenv()

try:
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_DATABASE')
        )

    cursor = conn.cursor()

except:
    clear_screen()

    print('\n[ Não foi possível se conectar ao banco de dados! Verifique a integridade do MySQL e tente novamente. ]')

    press_enter_to_continue()

    clear_screen()

    print('Programa encerrado...')

    exit()