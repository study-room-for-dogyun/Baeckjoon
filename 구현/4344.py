# https://www.acmicpc.net/problem/4344

C = int(input())
answer = []
for _ in range(C):

    std = list(map(int, input().split()))
    m = sum(std[1:]) / std[0]
    total = 0
    for i in std[1:]:
        if i > m:
            total += 1

    answer.append((total / std[0]) * 100)

for i in answer:
    if i < 10:
        print('{:0<5.5}%'.format(i))
    else:
        print('{:0<6.5}%'.format(i))
