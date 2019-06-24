jumlah_bayaran = float(input("sila masukkan jumlah bayaran: "))

if jumlah_bayaran in range(100, 301):
    jumlah_bayaran = jumlah_bayaran * 10 / 100
    print(jumlah_bayaran)
elif jumlah_bayaran > 300:
    jumlah_bayaran = jumlah_bayaran *20/100
    print(jumlah_bayaran)
    print("anda layak menerima sampul hari raya")
else:
    print(jumlah_bayaran)

