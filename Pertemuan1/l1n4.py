def cek_prima (angka):
    if angka > 1:
        for i in range (2, angka):
            if (angka % i) == 0:
                print (angka, "bukan bilangan prima")
                break
        else:
            print (angka, "adalah bilangan prima")
    else:
        print (angka, "bukan bilangan prima")

try:
    angka = int(input("Masukkan angka: "))
    cek_prima(angka)
except ValueError:
    print("Harap masukkan angka.")