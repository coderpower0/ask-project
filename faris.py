gred_a=18
gred_b=15
gred_c=10

berat_gred_a =float(input("sila masukkan berat gred a dalam kilogram :"))
berat_gred_b =float(input("sila masukkan berat gred b dalam kilogram :"))
berat_gred_c =float(input("sila masukkan berat gred c dalam kilogram :"))

harga_gred_a =gred_a*berat_gred_a
harga_gred_b =gred_b*berat_gred_b
harga_gred_c =gred_c*berat_gred_c

harga_gred_a =harga_gred_a * 15 /100

jum_ikan = harga_gred_a + harga_gred_b + harga_gred_c

print(jum_ikan)
