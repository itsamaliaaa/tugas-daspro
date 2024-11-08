""" Nama : Siti Amalia Putri
    NIM  : 2406274
    Kelas: 1 B
    Tugas: Menghitung Volume lingkaran
"""

def volumetabung(r, t):
    phi = 22/7 
    hasil = phi * (r ** 2) * t  
    return hasil  
r = int(input("Masukkan jari jari: "))
t = int(input("Masukkan tinggi: "))
print(volumetabung(r, t))