from __future__ import print_function

s = input("repl> ")
list = ["a","e","i","o","u"]
cmd = ["ls", "cat", "rev" ,"pwd"]
if s == "quit":
	print("",end='')
elif len(s) == 6:
	print("My length is 6")
elif s[0] in list:
	t = s[1]+s[2]+s[3]
	for i in range (4):
		print(t)
elif s in cmd:
	print("I know the command "+cmd[cmd.index(s)]+" !!")
elif s[0] == "0" and s[len(s)-1] != "9":
	for i in s:
		if i.isdigit():
			print(i)
