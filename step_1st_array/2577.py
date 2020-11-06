n = [int(input()) for _ in range(3)]

mul = str(n[0] * n[1] * n[2])
count = [0] * 10

for i in mul:
    count[int(i)] += 1

for i in count:
    print(i)