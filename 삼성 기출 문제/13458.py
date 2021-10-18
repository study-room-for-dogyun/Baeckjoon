# https://www.acmicpc.net/problem/13458
import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = N
for a in A:
    a -= B
    if a > 0:
        ans += math.ceil(a / C)

print(ans)
