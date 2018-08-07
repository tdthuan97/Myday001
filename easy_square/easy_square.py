x = int(input(""))
s = input("")
if x <= 0:
    print("Invalid value")
corner = s[0]
rowHead = s[1]
rowLast = s[2]
colLeft = s[3]
colRight = s[4]
for i in range(0, x):
    for j in range(0, x):
        if i == 0:
            if j == 0 or j == x-1:
                print(corner, end="")
            else:
                print(rowHead, end="")
        elif i == x-1:
            if j == 0 or j == x-1:
                print(corner, end='')
            else:
                print(rowLast, end='')
        else:
            if j == 0:
                print(colLeft, end='')
            elif j == x-1:
                print(colRight, end='')
            else:
                print(" ", end='')
    print("")
