from database.connection import cursor, conn

def verify_if_exits(date) -> bool:
    cursor.execute('SELECT Date FROM monitoring WHERE Date=%s', (date, ))

    if len(cursor.fetchall()) > 0:
        return True

    else:
        return False