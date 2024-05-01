price = int(input())
def vatCal(price):
    total = price+(price*7/100)
    return total


print(vatCal(price))