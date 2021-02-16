from itertools import combinations_with_replacement

n, m = map(int, input().split())

per = list(map(int, input().split()))
per.sort()

for i in combinations_with_replacement(per, m):
    for j in i:
        print(j, end=' ')
    print()