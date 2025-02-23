class manusia:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
    
    def hasil (self):
        print ("Nama:", self.nama)
        print ("Usia:", self.usia, "tahun")

def main ():
    a = input("Masukkan nama: ")
    b = input("Masukkan usia: ")
    c = manusia(a, b)
    c.hasil()
    
if __name__ == "__main__":
    main()
