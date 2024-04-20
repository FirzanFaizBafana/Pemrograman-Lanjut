def hitung_nilai_akhir(tugas, uts, uas):
    nilai_akhir = 0.25 * tugas + 0.35 * uts + 0.40 * uas
    return nilai_akhir

def konversi_nilai(nilai_akhir):
    if nilai_akhir > 85:
        return 'A'
    elif nilai_akhir > 80:
        return 'A-'
    elif nilai_akhir > 75:
        return 'B+'
    elif nilai_akhir > 70:
        return 'B'
    elif nilai_akhir > 65:
        return 'B-'
    elif nilai_akhir > 60:
        return 'C+'
    elif nilai_akhir > 55:
        return 'C'
    elif nilai_akhir > 50:
        return 'C-'
    elif nilai_akhir > 30:
        return 'D'
    else:
        return 'E'

def main():
    print("Selamat Datang di Aplikasi perhitungan nilai Mahasiswa")
    tugas = float(input("Silahkan Masukkan nilai tugas Anda: "))
    uts = float(input("Silahkan Masukkan nilai UTS Anda: "))
    uas = float(input("Silahkan Masukkan nilai UAS Anda: "))

    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    nilai_huruf = konversi_nilai(nilai_akhir)

    print("Nilai akhir:", nilai_akhir)
    print("Dalam huruf:", nilai_huruf)

if __name__ == "__main__":
    main()
