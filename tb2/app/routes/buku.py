from fastapi import APIRouter, HTTPException
from app.models.buku import Buku
from app.database.connection import koneksi_db, close_db

router = APIRouter()

@router.get("/buku/{id}")
def get_buku(id: int):
    cursor, connection = koneksi_db()
    try:
        cursor.execute("SELECT * FROM buku WHERE id = %s", (id,))
        buku = cursor.fetchone()
        if not buku:
            raise HTTPException(status_code=404, detail="Buku tidak ditemukan")
        return buku
    except Exception as e:
        print(f"Error getting book: {e}")
        raise HTTPException(status_code=500, detail="Gagal mendapatkan buku")
    finally:
        close_db(cursor, connection)

@router.post("/buku")
def create_buku(buku: Buku):
    cursor, connection = koneksi_db()
    try:
        sql = """
        INSERT INTO buku (judul, penulis, penerbit, tahun_terbit, konten, iktisar)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        val = (buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, buku.konten, buku.iktisar)
        cursor.execute(sql, val)
        connection.commit()
        new_book_id = cursor.lastrowid
        return {"message": "Buku baru telah dibuat", "id": new_book_id}
    except Exception as e:
        print(f"Error creating book: {e}")
        raise HTTPException(status_code=500, detail="Gagal membuat buku")
    finally:
        close_db(cursor, connection)
