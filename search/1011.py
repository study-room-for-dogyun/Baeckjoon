# https://www.acmicpc.net/problem/1011
import math

t = int(input())

for _ in range(t):

    s, e = map(int, input().split())
    distance = e - s
    maxi = round(math.log2(distance))    # 최대 갈 수 있는 거리

    print(maxi)