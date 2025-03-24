from abc import ABC, abstractmethod

class Buku(ABC):
    def __init__ (self, nama, judul):
        self.nama = nama
        self.judul = judul 

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def daftar(self):
        pass

class Yes(Buku):
    def info(self):
        print(f"Ebook {self.judul} ditemukan dalam perpustakaan.")

    def daftar(self):
        print(f"{self.nama} menambahkan {self.judul} ke dalam daftar membaca.")

class No(Buku):
    def info(self):
        print(f"Ebook {self.judul} tidak ditemukan dalam perpustakaan.")

    def daftar(self):
        pass

y = Yes ("Zed", "Laut Bercerita")
n = No ("Zed", "Jakarta Sebelum Pagi")

for i in (y, n):
    i.info()
    i.daftar()