try:
    principal = float(input("sila masukkan jumlah pinjaman yang diambil: "))
    interest_rate = float(input("sila masukan kadar faedah: "))
    duration = float(int(input("sila masukkan tempoh bayaran balik dalam tahun: ")))
except ValueError:
    print("oops... that's not a valid number")


def monthly_payment(principal, interest_rate, duration):
    if duration >= 1:
        month = duration * 12
    else:
        pass
    interest_rate = interest_rate / 100
    interest = interest_rate * principal * duration
    principal = interest + principal
    monthly_payment = principal / month
    monthly_payment = float(format(monthly_payment, '.2f'))

    return monthly_payment

try:
    monthly = monthly_payment(principal, interest_rate, duration)
except NameError:
    pass

try:
    print("jumlah bayaran bulanan yang perlu anda bayar ialah:", monthly)
except NameError:
    pass
