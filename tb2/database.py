import mysql.connector

def koneksi_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tugas"
    )
    mycursor = mydb.cursor()
    return mycursor, mydb

def close_db(cursor, db):
    cursor.close()
    db.close()