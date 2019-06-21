try:
    loan = float(input("sila masukkan jumlah pinjaman yang diambil: "))
    interest_rate = float(input("sila masukan kadar faedah: "))
    year = float(int(input("sila masukkan tempoh bayaran balik dalam tahun: ")))
except ValueError:
    print("oops... that's not a valid number")


def monthly_payment(loan, interest_rate, year):
    month = year * 12
    interest_rate = interest_rate / 100
    interest = interest_rate * loan * year
    loan = interest + loan
    monthly_payment = loan / month

    return monthly_payment


try:
    monthly = monthly_payment(loan, interest_rate, year)
except NameError:
    pass

try:
    print("jumlah bayaran bulanan yang perlu anda bayar ialah:", format(monthly, '.2f'))
except NameError:
    pass
