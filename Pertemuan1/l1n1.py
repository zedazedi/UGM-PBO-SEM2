def hitung(n):
    for i in range (n, -1, -1):
        print (i, end = " ")
try:
    n = int(input("Masukkan angka: "))
    hitung(n)
except ValueError:
    print("Harap masukkan angka.")