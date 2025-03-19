#kelas Pangkat berisi metode untuk mencari hasil pangkat
class Pangkat:
    def __init__(self, angka):
        self.angka = angka

    def __pow__(self, besar_pangkat):
        return self.angka**besar_pangkat.angka #rumus mencari hasil pemangkatan
    
p1 = Pangkat(2)
p2 = Pangkat(6)
print("Hasil pemangkatan:", p1**p2)