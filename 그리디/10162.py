t = int(input())

bt = [300, 60, 10]
count = [0, 0, 0]

if t % 10 != 0:
	print(-1)
else:

	for i in range(len(bt)):
		if t >= bt[i]:
			count[i] += t // bt[i]
			t %= bt[i]
		
	for i in count:
		print(i, end=" ")