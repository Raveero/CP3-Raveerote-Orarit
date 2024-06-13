orderList = []
priceList = []
total = 0
while True:
    order = input("What do you want to order?: ")
    if order.lower() == "exit":
        break
    else:
        price = int(input("Price: "))
        orderList.append(order)
        priceList.append(price)
        total += price


def show_bill():
    print("---Bill---")
    for num in range(len(orderList)):
        print(orderList[num], priceList[num], "THB")
    print("Total price:", total, "THB")


show_bill()