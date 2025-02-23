class persegi:
    def __init__ (self, Sisi):
        self.Sisi = Sisi

    def luas (self):
        luas = self.Sisi*self.Sisi
        print("Luas persegi adalah", luas, "cm^2")
    
    def keliling(self):
        kel = 4*self.Sisi
        print("Keliling persegi adalah", kel, "cm")

def main ():
    a = int(input("Masukkan panjang sisi persegi: "))
    b = persegi(a)
    b.luas()
    b.keliling()

if __name__ == "__main__":
    main()