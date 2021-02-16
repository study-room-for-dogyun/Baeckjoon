from itertools import product

n, m = map(int, input().split())

per = list(map(int, input().split()))
per.sort()

for i in product(per, repeat=m):
    for j in i:
        print(j, end=' ')
    print()