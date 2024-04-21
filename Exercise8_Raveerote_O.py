keyUser = "TOTO"
keyPass = "Raveerote"
User = input("Enter Username:")
Pass = input("Enter Password:")
if User == keyUser and Pass == keyPass:
    print("Login Successfully")
    print("Welcome TO 1234 Shop")
    print("------Product list--------")
    print("1.Apple 50 THB")
    print("2.Banana 40 THB")
    print("3.Orange 60 THB")
    userSelected = int(input("Enter the number of product >>"))
    amount = int(input("Enter the amount of product >>"))
    if userSelected == 1:
        print("Total price will be: ", 50 * amount, "THB")
    elif userSelected == 2:
        print("Total price will be: ", 40 * amount, "THB")
    elif userSelected == 3:
        print("Total price will be: ", 60 * amount, "THB")
    print("Thankyou For use 1234 shop")
else:
    print("error")