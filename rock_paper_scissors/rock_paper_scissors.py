p1 = input("Player 1? ")
p2 = input("Player 2? ")
test = (p1, p2)
r = 'rock'
s = 'scissors'
p = 'paper'

if p1 in (r, s, p) and p2 in (r, s, p):
    if(p1 == p2):
        print("Draw.")
    elif test in ((r, s), (s, p), (p, r)):
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    print("Error.")
