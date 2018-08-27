x = int(input("How many squares do you need?\n"))
k = 4 * x - 1
start = 1
mid = k // 2 + 1
end = k
rev = 0;
flag = 0;
one = False;
for i in range(1, k + 1):
	for j in range(1, k + 1):
		if i % 2 == 1:
			if j >= start and j <= end:
				print("#", end = '')
			else:
				if j % 2 == 1:
					print("#", end = '')
				else:
					print(" ", end = '')
		else:
			if j <= start or j >= end:
				if j % 2 == 1:
					print("#", end = '')
				else:
					print(" ", end = '')
			else:
				print(" ", end = '')
	if i % 2 == 0 and rev == 0:
		if i == mid:
			rev = 1;
			start = mid - 1;
			end = mid + 1
		elif rev == 0:
			start += 2
			end -= 2
	if i % 2 == 1 and rev == 1:
		if rev == 1:
			start -= 2
			end += 2
	print("")
			
