class Siswa:
    def __init__ (self, Nama, NISN, Angkatan):
        self.Nama = Nama
        self.NISN = NISN
        self.Angkatan = Angkatan

    def tampilkan_data (self):
        print("Nama:", getattr(self, 'Nama', 'Nama tidak ditemukan'))
        print("NISN:", str(self.NISN))
        print("Angkatan:", str(self.Angkatan))

Siswa1 = Siswa("Zed", 66789, 2021)
Siswa1.tampilkan_data()
print("")
del Siswa1.Nama
Siswa1.tampilkan_data()
print("")
del Siswa1
Siswa1.tampilkan_data()
