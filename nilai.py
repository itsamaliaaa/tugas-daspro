""" Nama : Siti Amalia Putri
    NIM  : 2406274
    Kelas: 1 B
    Tugas: Menghitung nilai total dan nilai rata-rata
"""

def hitung_nilai():
    nilai_list = []
    while True:
        nilai_input = input("Masukkan nilai (tekan Enter untuk selesai): ")
        if not nilai_input:
            break 
        nilai_list.append(int(nilai_input))  

    total = sum(nilai_list)
    rata_rata = total / len(nilai_list)
    print("Total Nilai:", total)
    print("Rata-Rata Nilai:", rata_rata)

hitung_nilai()
