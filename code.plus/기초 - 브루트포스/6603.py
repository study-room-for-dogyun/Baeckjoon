# https://www.acmicpc.net/problem/6603

from itertools import combinations

while True:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break

    for i in combinations(n[1:], 6):
        for k in i:
            print(k, end=' ')
        print()
    print()