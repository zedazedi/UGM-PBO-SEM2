def keliling_lingkaran (r):
    kel = 2*3.14*r
    print (f"Keliling lingkaran adalah {kel} cm")

def luas_lingkaran (r):
    l = 3.14*r*r
    print(f"Luas lingkaran adalah {l} cm")

r = int(input("Masukkan jari-jari lingkaran (dalam cm): "))
keliling_lingkaran(r)
luas_lingkaran(r)
