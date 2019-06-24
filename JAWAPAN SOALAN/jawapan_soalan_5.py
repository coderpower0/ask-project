harga_beli = float(input("sila masukkan harga beli barang: "))
harga_jual = float(input("sila masukkan harga jual barang: "))

beza = harga_jual - harga_beli

if beza < 0:
    print("kerugian adalah RM", format((beza * -1), '.2f'))
elif beza > 0:
    print("keuntungan ialah RM", format(beza, '.2f'))
else:
    print("tiada keuntungan atau kerugian")