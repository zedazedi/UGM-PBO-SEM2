class Passenger:
    TITLES = ("Mr", "Mrs", "Ms") #class attribute

    def __init__ (self, title, fname, lname):
        if title not in self.TITLES:
            raise ValueError ("%s is not a valid title." % title)
        
        self.title = title #instance attribute
        self.fname = fname #instance attribute
        self.lname = lname #instance attribute

#Pembuatan Objek
p1 = Passenger("Mr", "Kiewlamphone", "Souvanlith")
#mengakses class attribute dari object
print(p1.TITLES)
#mengakses class attribute dari kelas
print(Passenger.TITLES)
#mengakses instance attribute dari objek
print(p1.title)
#mengakses instance attribute dari kelas
