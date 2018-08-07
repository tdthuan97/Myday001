result = int(input("What is the result? "))
print("OK, let's begin\n")
ok = 0
for i in range(10, -1, -1):
    remain = ""
    spe = ""
    if(i == 5):
        remain = "(Half way done) "
    elif(i == 0):
        remain = "(Last guess) "
    else:
        remain = "(" + str(i) + " left) "
    guess = int(input("Your gress? "+remain))
    if(guess < result):
        if(result - guess > 50):
            print("It's way more.")
        else:
            print("It's more.")
    elif(guess > result):
        if(guess - result > 50):
            print("It's way less.")
        else:
            print("It's less.")
    else:
        print("Congrats !")
        ok = 1
        break
if(ok == 0):
    print("You lose :(")
