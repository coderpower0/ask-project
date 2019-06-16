# TODO: add algorithm that calculate percent rate
# TODO: add algorithm that calculate interest rate
# TODO: add algorithm that calculate monthly payment


mode = int(input("sila masukkan 1 untuk mengira kadar peratus 2 untuk mengira kadar faedah \n3 untuk mengira ansuran bulanan: "))
price = float(input("sila masukkan harga kereta: "))
interest = float(input("sila masukkan kadar faedah: "))
year = float(input("sila masukkan tempoh pembayaran: "))

interest = interest / 100
year = year * 12


def mode(mode):
    if mode == 1:
        pass
    elif mode == 2:
        pass
    elif mode == 3:
        pass
    else:
        pass


def percent_rate():
    pass


def interest_rate():
    pass


def monthly_payment():
    interest_rate = (price * interest * (year / 12) + price)
    interest_rate = interest_rate / year
    return interest_rate


print(format(monthly_payment(), ".2f"))
