class Sim:
    def info(self):
        print("SIM B diklasifikasikan menjadi dua jenis sesuai dengan tipe kendaraan yang dikendarai.")
    def klasifikasi(self):
        print("Terdapat dua jenis SIM B, yaitu SIM B1 dan SIM B2.")

class Sim_b1(Sim):
    def klasifikasi(self):
        print("SIM B1: pengemudi kendaraan penumpang atau pengangkut barang dengan berat kendaraan > 3.500 kg.")

class Sim_b2(Sim):
    def klasifikasi(self):
        print("SIM B2: pengemudi kendaraan dengan berat kendaraan > 1.000 kg.")


obj_sim = Sim()
obj_b1 = Sim_b1()
obj_b2 = Sim_b2()

obj_sim.info()
obj_sim.klasifikasi()

obj_b1.info()
obj_b1.klasifikasi()

obj_b2.info()
obj_b2.klasifikasi()