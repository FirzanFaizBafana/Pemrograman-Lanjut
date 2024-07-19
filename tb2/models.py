from pydantic import BaseModel, Field

class Buku(BaseModel):
    judul: str = Field(...)
    penulis: str = Field(...)
    penerbit: str = Field(...)
    tahun_terbit: int = Field(...)
    konten: str = Field(...)
    iktisar: str = Field(...)

    def read(self, nomor_halaman_awal, nomor_halaman_akhir):
        if nomor_halaman_awal > nomor_halaman_akhir:
            raise ValueError("Nomor halaman awal tidak boleh lebih besar dari nomor halaman akhir")
        for halaman in range(nomor_halaman_awal, nomor_halaman_akhir + 1):
            print(f"Halaman {halaman}:")
            print(self.konten[halaman])

    def __str__(self):
        return f"{self.judul} oleh {self.penulis}"