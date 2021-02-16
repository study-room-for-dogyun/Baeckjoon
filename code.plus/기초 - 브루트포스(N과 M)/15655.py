from itertools import combinations

n, m = map(int, input().split())

per = list(map(int, input().split()))
per.sort()

for i in combinations(per, m):
    for j in i:
        print(j, end=' ')
    print()