from itertools import permutations

n, m = map(int, input().split())

per = list(map(int, input().split()))
per.sort()

for i in permutations(per, m):
    for j in i:
        print(j, end=' ')
    print()