n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse = True)

count = 0


for coin in coins:
    if n >= coin:
        count += n // coin

        n %= coin

    if n == 0:
        break

    count += 1


print(count)