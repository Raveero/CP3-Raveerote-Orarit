num = int(input())
base = 0
for x in range(num):
    print(" "*(num-(x+1))+"*"*(2*x+1))

while num > 0:
    print(" " * (num-1)+"*" * (base*2+1))
    num -= 1
    base += 1