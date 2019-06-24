jumlah_bayaran = float(input("sila masukkan jumlah bayaran: "))

if jumlah_bayaran in range(100, 301):

    jumlah_bayaran = jumlah_bayaran * 10 / 100
    print("RM", format(jumlah_bayaran, '.2f'))

elif jumlah_bayaran > 300:

    jumlah_bayaran = jumlah_bayaran * 20 / 100
    print("RM", format(jumlah_bayaran, '.2f'))
    print("anda layak menerima sampul hari raya")

else:

    print("RM", format(jumlah_bayaran, '.2f'))
