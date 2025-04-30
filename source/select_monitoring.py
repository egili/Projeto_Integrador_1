from database.connection import cursor
import datetime

def select_all_monitoring():
    cursor.execute("SELECT * FROM monitoring;")

    return cursor.fetchall()