from itertools import combinations 

t = int(input())

n = [list(map(int, input().split())) for _ in range(t)]

def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    
    return a


for i in n:
    result = 0
    for j in list(combinations(i[1:], 2)):
        result += gcd(j[0], j[1])
    
    print(result)