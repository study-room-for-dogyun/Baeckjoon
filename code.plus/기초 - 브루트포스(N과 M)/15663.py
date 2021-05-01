# https://www.acmicpc.net/problem/15663

from itertools import permutations

n, m = map(int, input().split())

per = list(map(int, input().split()))
per.sort()


temp = set()

for i in permutations(per, m):
    if i not in temp:
        for j in i:
            print(j, end=' ')
        print()
        temp.add(i)
