class Siswa:
    def __init__ (self, Nama, NISN, Angkatan):
        self.Nama = Nama
        self.NISN = NISN
        self.Angkatan = Angkatan

    def tampilkan_data (self):
        print("Nama:", self.Nama)
        print("NISN:", str(self.NISN))
        print("Angkatan:", str(self.Angkatan))

Siswa1 = Siswa("Zed", 66789, 2021)
Siswa1.tampilkan_data()