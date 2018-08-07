from __future__ import print_function
x = int(input("What pyramid size do you want?\n"))
if x % 2 == 0:
    x -= 1
k = x // 2
t = k
count = 0
while k < x:
    for i in range(k + 1):
        if i >= t:
            print("#", end='')
        else:
            print(" ", end='')
    k += 1
    t -= 1
    print("")
