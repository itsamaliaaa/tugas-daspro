""" Nama : Siti Amalia Putri
    NIM  : 2406274
    Kelas: 1 B
"""

def fibonacci(n):
    a, b = 0, 1  
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  

n = int(input("\nMasukkan jumlah angka Fibonacci: "))

print("\nDeret Fibonacci:", end=" ")
fibonacci(n)
print()  