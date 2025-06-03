from database.connection import cursor

def select_all_monitoring():
    cursor.execute("SELECT * FROM monitoring ORDER BY Date ASC;")

    monitoring_list = cursor.fetchall()
    classifications_list = []

    for date in monitoring_list:
        cursor.execute("SELECT * FROM monitoring_classifications WHERE Date=%s;", (date[0], ))

        classifications_list.append(cursor.fetchall())

    return [monitoring_list, classifications_list]

def select_monitoring_dates():
    cursor.execute("SELECT DATE FROM monitoring ORDER BY Date ASC;")

    return cursor.fetchall()

def select_specif_monitoring(date):
    cursor.execute("SELECT * FROM monitoring WHERE Date=%s", (date, ))

    monitoring_list = cursor.fetchall()
    classifications_list = []

    for date in monitoring_list:
        cursor.execute("SELECT * FROM monitoring_classifications WHERE Date=%s;", (date[0], ))

        classifications_list.append(cursor.fetchall())

    return [monitoring_list, classifications_list]