import mysql.connector

def koneksi_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pl"
    )
    mycursor = mydb.cursor(dictionary=True)
    return mycursor, mydb

def close_db(cursor, db):
    cursor.close()
    db.close()
