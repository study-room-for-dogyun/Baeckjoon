# https://www.acmicpc.net/problem/10972
from itertools import permutations

n = int(input())
p = list(map(int, input().split()))

def x():
    check = False
    for i in permutations(range(1, n+1), n):
        if check:
            return i

        if list(i) == p:
            check = True
    
    return [-1]

for i in x():
    print(i, end=" ")