# https://www.acmicpc.net/problem/9095

from itertools import product

t = int(input())
n = [int(input()) for _ in range(t)]

def ju(x):
    result = 0
    num = [1, 2, 3]

    for i in range(1, x+1):

        for j in product(num, repeat=i):
            
            if sum(j) == x:
                result += 1

    return result

for i in n:
    print(ju(i))