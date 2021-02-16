from itertools import combinations_with_replacement

n, m = map(int, input().split())

for i in combinations_with_replacement([t for t in range(1, n+1)], m):
    for j in i:
        print(j, end=' ')
    print()