from database.connection import conn, cursor

def delete_from_db(date):
    cursor.execute("DELETE FROM monitoring WHERE Date=%s", (date, ))
    
    conn.commit()