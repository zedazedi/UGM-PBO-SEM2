while (True):
    niu = input("Masukkan NIU (6 digit): ")
    if len(niu) != 6:
        print("NIU tidak ditemukan, mohon coba kembali.")
    else:
        tugas = int(input("Masukkan nilai tugas: "))
        laporan = int(input("Masukkan nilai laporan: "))
        jumlah = tugas + laporan 
        avr = jumlah / 2
        print("Rata-rata nilai tugas & laporan anda adalah", avr)
        if avr < 40:
            print ("Nilai anda: K")
        else:
            uji = int(input("Masukkan nilai ujian: "))
            bobot_tugas = tugas / 4
            bobot_laporan = laporan / 4
            bobot_ujian = uji / 2
            akhir = bobot_tugas + bobot_laporan + bobot_ujian
            if akhir < 50:
                nilai = "E"
            elif 50 <= akhir < 60:
                nilai = "D"
            elif 60 <= akhir < 70:
                nilai =  "C"
            elif 70 <= akhir < 80:
                nilai = "B"
            elif 80 <= akhir <= 100:
                nilai = "A"
            print (f"Nilai akhir anda adalah {akhir} ({nilai})", )
        break
    