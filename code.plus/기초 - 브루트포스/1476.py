n = list(map(int, input().split()))

esm = [15, 28, 19]

start = [1, 1, 1]

result = 1


while n != start:

    for i in range(3):
        start[i] += 1
        if start[i] > esm[i]:
            start[i] = 1

    result += 1

print(result)