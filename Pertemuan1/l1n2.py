def cek_cuaca(suhu):
    if suhu <0:
        keterangan = "Kondisi Cuaca: Membeku"
    elif suhu < 10:
        keterangan = "Kondisi Cuaca: Sangat Dingin"
    elif suhu < 20:
        keterangan = "Kondisi Cuaca: Sejuk"
    elif suhu < 30:
        keterangan = "Kondisi Cuaca: Hangat"
    elif suhu < 40:
        keterangan = "Kondisi Cuaca: Panas"
    else:
        keterangan = "Kondisi Cuaca: Sangat Panas"
    print (keterangan)

try:
    suhu = float(input("Masukkan suhu (dalam Celcius): "))
    cek_cuaca(suhu)
except ValueError:
    print("Harap memberikan input hanya berupa angka.")