# TODO: add algorithm that calculate percent rate
# TODO: add algorithm that calculate interest rate
# TODO: add algorithm that calculate monthly payment

price = float(input("sila masukkan harga kereta: "))
interest_rate = float(input("sila masukkan kadar faedah: "))
year = float(input("sila masukkan tempoh pembayaran: "))

interest_rate = interest_rate / 100
month = year * 12


def main():
    mode = int(input(
        "sila masukkan 1 untuk mengira kadar peratus 2 untuk mengira kadar faedah \n3 untuk mengira ansuran bulanan: "))

    if mode == 1:
        print(format(percent_rate(), '.2f'))
    elif mode == 2:
        print(format(interest(), '.2f'))
    elif mode == 3:
        print(format(monthly_payment(), '.2f'))
    else:
        pass


def percent_rate():
    pass


def interest():
    interest = price * interest_rate * year
    return interest


def monthly_payment():
    monthly_payment = (price * interest_rate * year + price)
    monthly_payment = monthly_payment / month
    return monthly_payment


main()
pass
