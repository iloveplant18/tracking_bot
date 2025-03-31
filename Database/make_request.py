import sqlite3

def make_request(request):
    with sqlite3.connect("data/db.db") as connection:
        cursor = connection.cursor()
        cursor.execute(request)
        return cursor.fetchall()
