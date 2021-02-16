from itertools import product

n, m = map(int, input().split())

for i in product([t for t in range(1, n+1)], repeat=m):

    for j in i:
        print(j, end=" ")
    print()