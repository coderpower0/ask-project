try:
    principal = float(input("sila masukkan jumlah pinjaman yang diambil: "))
    interest_rate = float(input("sila masukan kadar faedah: "))
    duration = float(int(input("sila masukkan tempoh bayaran balik dalam tahun: ")))
except ValueError:
    print("oops... that's not a valid number")


def monthly_payment(principal, interest_rate, duration):
    month = duration * 12
    interest_rate = interest_rate / 100
    interest = interest_rate * principal * duration
    principal = interest + duration
    monthly_payment = principal / month

    return monthly_payment

try:
    monthly = monthly_payment(principal, interest_rate, duration)
except NameError:
    pass

try:
    print("jumlah bayaran bulanan yang perlu anda bayar ialah:", format(monthly, '.2f'))
except NameError:
    pass
