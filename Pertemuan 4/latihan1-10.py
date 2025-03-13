class Orang:
    def __init__(self, nama_depan, nama_belakang, no_id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.no_id = no_id

class Mahasiswa (Orang):
    SARJANA = "Mahasiswa Sarjana"
    MASTER = "Mahasiswa Master"
    DOKTOR = "Mahasiswa Doktor"

    def __init__ (self, jenjang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.jenjang = jenjang
        self.matkul = []

    def enrol (self, *mata_kuliah):
        self.matkul.extend (mata_kuliah)
        print(self.jenjang, "Nomor ID", self.no_id, self.nama_depan, self.nama_belakang,  "mengambil mata kuliah", ", ".join(self.matkul))
    
class Karyawan (Orang):
    TETAP = "Pegawai tetap" 
    TDK_TETAP = "Pegawai tidak tetap"

    def __init__ (self, status, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status = status

class Dosen (Karyawan):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.matkul_diajar = []

    def mengajar (self, *mata_kuliah ):
        self.matkul_diajar.extend (mata_kuliah)
        print(self.status, "Nomor ID", self.no_id, self.nama_depan, self.nama_belakang, "mengajar mata kuliah", ", ".join(self.matkul_diajar))
    
bowo = Mahasiswa(Mahasiswa.SARJANA, "Bowo", "Nugroho", "987654")
bowo.enrol("Basis Data")

rizki = Dosen(Karyawan.TETAP, "Rizki", "Setiabudi", "456789") 
rizki.mengajar("Statistik")

class Pelajar:
    def __init__ (self):
        self.matkul = []

    def enrol(self, *mata_kuliah):
        self.matkul.extend (mata_kuliah)
        print(self.nama_depan, self.nama_belakang, "dengan Nomor ID", self.no_id, "mengambil mata kuliah", ", ".join(self.matkul))

class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar (self, *matkul_ajar):
        self.matkul_diajar.extend (matkul_ajar)
        print(self.nama_depan, self.nama_belakang,  "dengan Nomor ID", self.no_id, "mengajar mata kuliah", ", ".join(self.matkul_diajar))

class Asdos (Orang, Pelajar, Pengajar):
    def __init__ (self, *args, **kwargs):
        super().__init__ (*args, **kwargs)
        Pelajar.__init__(self)
        Pengajar.__init__(self)

uswatun = Asdos("Uswatun", "Hasanah", "456456")
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")

