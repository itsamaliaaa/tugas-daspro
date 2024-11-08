""" Nama : Siti Amalia Putri
    NIM  : 2406274
    Kelas: 1 B
"""
def login():
    password_sistem = "Latihan"  
    kesempatan = 3  

    while kesempatan > 0:
        password_input = input("\nPassword: ")

        if password_input == password_sistem:
            print("\nLogin berhasil!\n")
            return True  
        else:
            kesempatan -= 1
            if kesempatan > 0:
                print(f"\nPassword salah! Anda memiliki {kesempatan} kesempatan lagin\n")
            else:
                print("\nKesempatan habis, Anda telah memasukkan password yang salah 3 kali\n")
                return False 

def menu_login():
    print("\nSelamat datang di menu login!")
    print("\nUsername: Daspro2024")
    
    login()

menu_login()
