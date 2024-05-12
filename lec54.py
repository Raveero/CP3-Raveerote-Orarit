

def login():
    username = input()
    password = input()
    if username == "TOTO" and password == "1234":
        return True
    else:
        return False
def menu():
    print("Welcome to Gusto shop")
    print("Select your service")
    print("1. VatCal")
    print("2. PriceCal")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCal(price):
    return print(price+(price*7/100))

def priceCal():
    x = int(input("1)"))
    y = int(input("2)"))
    return vatCal(x+y)

if login() == True:
    menu()
    c = menuSelect()
    if c == 1:
        price = int(input())
        vatCal(price)
    elif c == 2:
        priceCal()
    else:
        print("Please reselect the Service")
        menuSelect()
else :
    print("The Username or Password may not corrected")
