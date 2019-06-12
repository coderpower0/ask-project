grade_A_fish = float(input("sila masukkan berat ikan yang dibeli gred a dalam kilogram: "))
grade_B_fish = float(input("sila masukkan berat ikan yang gred b dibeli dalam kilogram: "))
grade_C_fish = float(input("sila masukkan berat ikan gred c yang dibeli dalam kilogram: "))

grade_A_sum = grade_A_fish * 18
grade_B_sum = grade_B_fish * 15
grade_C_sum = grade_C_fish * 10

fish_sum = grade_A_sum + grade_B_sum + grade_C_sum

if grade_A_fish != 0:
    fish_sum = fish_sum * (0.15)

print(format(fish_sum, '.2f'))
