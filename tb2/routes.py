from fastapi import FastAPI, HTTPException
from models import Buku
from database import koneksi_db, close_db

app = FastAPI()

@app.get("/buku/{id}")
def get_buku(id: int):
    cursor, db = koneksi_db()
    cursor.execute(f"SELECT * FROM buku WHERE id = {id}")
    buku = cursor.fetchone()
    close_db(cursor, db)
    if not buku:
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan")
    return Buku(buku[1], buku[2], buku[3], buku[4], buku[5], buku[6])

@app.post("/buku")
def create_buku(buku: Buku):
    cursor, db = koneksi_db()
    sql = "INSERT INTO buku (judul, penulis, penerbit, tahun_terbit, konten, iktisar) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, buku.konten, buku.iktisar)
    cursor.execute(sql, val)
    db.commit()
    cursor.execute("SELECT LAST_INSERT_ID()")
    id = cursor.fetchone()[0]
    close_db(cursor, db)
    return get_buku(id)
