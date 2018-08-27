x = int(input("What is the size of your train? "))
if x < 0:
	print("Don\'t be so negative.")
elif x > 0:
	head =   ' _________________________ '
	body =   '|]||[]_[]_[]|||[]_[]_[]||[|'
	bottom = '\==o-o======o-o======o-o==/'
	train_head = ''
	train_body = ''
	train_bottom = ''
	for i in range(x):
		print(i)
		if i == x-1:
			train_head += head[:23] + '>' + head[24:]
			train_body += body
			train_bottom += bottom
		else:
			train_head += head + ' '
			train_body += body + ' '
			train_bottom += bottom + '_'
	print(train_head + '\n' + train_body + '\n' + train_bottom)

Write a program tchou_tchou.py that prints a train of various sizes.

$ python3 tchou_tchou.py
What is the size of your train? 0
$ python3 tchou_tchou.py
What is the size of your train? 1
 ______________________>__
|]||[]_[]_[]|||[]_[]_[]||[|
\==o-o======o-o======o-o==/
$ python3 tchou_tchou.py
What is the size of your train? 2
 _________________________   ______________________>__
|]||[]_[]_[]|||[]_[]_[]||[| |]||[]_[]_[]|||[]_[]_[]||[|
\==o-o======o-o======o-o==/_\==o-o======o-o======o-o==/
$ python3 tchou_tchou.py
What is the size of your train? -1
Don't be so negative.


