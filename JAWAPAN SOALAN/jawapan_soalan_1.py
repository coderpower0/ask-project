from math import pi

radius = float(input("sila masukkan jejari: "))
sloping = float(input("sila masukkan panjang sisi sendeng kon: "))

surface_area = ((pi*radius*sloping) + pi*(radius**2))
volume = (1 / 3) * pi * radius * sloping

print("luas kon ialah", format(surface_area, '.2f'))
print("isipadu kon ialah", format(volume, '.2f'))
