from pydantic import BaseModel

class Buku(BaseModel):
    judul: str
    penulis: str
    penerbit: str
    tahun_terbit: int
    konten: str
    iktisar: str
