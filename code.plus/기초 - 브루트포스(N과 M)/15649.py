from itertools import permutations

n, m = map(int, input().split())

for i in permutations([i for i in range(1, n+1)], m):
    
    for j in i:
        print(j, end=" ")
    print()