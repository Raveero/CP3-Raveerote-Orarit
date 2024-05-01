
def login():
    username = input()
    password = input()
    if username == "TOTO" and password == "1234":
        return menu()
    else:
        return print("error")
def menu():
    print("1. VatCal")
    print("2. PriceCal")
    return menuSelect()
def menuSelect():
    userSelected = int(input())
    if userSelected == 1:
        return vatCal()
    elif userSelected == 2:
        return priceCal()
    else:
        return menu()
def vatCal():
    price = int(input())
    return print(price+(price*7/100))

def priceCal():
    x = int(input("1)"))
    y = int(input("2)"))
    print(x+y)
    vatCal()

login()