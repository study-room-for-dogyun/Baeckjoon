n, k = map(int, input().split())

coins = list(int(input()) for _ in range(n))

count = 0
while coins:
	coin = coins.pop()

	if k >= coin:
		count += k // coin
		k = k % coin

print(count)