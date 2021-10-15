# https://www.acmicpc.net/problem/17281

from itertools import permutations

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in permutations(range(9), 9):
    if i[3] == 4:
        print(i)