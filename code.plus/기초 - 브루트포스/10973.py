# https://www.acmicpc.net/problem/10973
from itertools import permutations

n = int(input())
per = list(map(int, input().split()))
print(per)
for i in range(n-1, 0, -1):
    
    if per[i] > per[i-1]:
        x = i-1
        y = i

        for j in range(n-1, x, -1):
            if per[j] > per[x]:
                per[j], per[x] = per[x], per[j]
                per = per[:y+1] + sorted(per[y+1:])
                break

print(per)

