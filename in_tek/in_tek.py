x = int(input("Value? "))
a = x
for i in range(1, x + 1):
    if i % 5 == 0 and i % 9 == 0:
        print("InTek")
    elif i % 9 == 0:
        print("Tek")
    elif i % 5 == 0:
        print("In")
    else:
        print(i)
