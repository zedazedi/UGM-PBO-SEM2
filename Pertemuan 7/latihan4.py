def add_topping(cls):
    def topping(self, varian):
        self.varian = varian
        print(f"Kamu menambahkan topping {varian}")
    
    cls.topping = topping #Menambahkan metode topping ke dalam kelas
    return cls #Mengembalikan kelas yang telah dimodifikasi

@add_topping
class Susu:
    def __init__ (self, rasa):
        self.rasa = rasa

    def beli (self):
        print(f"Kamu membeli susu rasa {self.rasa} 🧋")

#Membuat objek dari kelas Susu
a = Susu("vanila")
a.beli()
a.topping("oreo crumbs") #Menambahkan topping ke susu
