n = int(input())

change = 1000 - n
coins = [1, 5, 10, 50, 100, 500]

count = 0
while coins:
	coin = coins.pop()
	if coin <= change:
		count += change // coin
		change %= coin

print(count)