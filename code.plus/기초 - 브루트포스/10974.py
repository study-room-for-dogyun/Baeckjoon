# https://www.acmicpc.net/problem/10974

from itertools import permutations

n = int(input())

for i in permutations([i for i in range(1, n+1)]):
    print(*i)