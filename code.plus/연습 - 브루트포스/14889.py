# https://www.acmicpc.net/problem/14889
from itertools import combinations, permutations

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = 9999999

for t1 in combinations(list(range(0, n)), n//2):
    total1 = 0
    total2 = 0

    if t1[0] != 0:
        break

    t2 = list(range(n))
    for i in t1:
        t2.remove(i)
    
    for i in combinations(t1, 2):
        total1 += graph[i[0]][i[1]] + graph[i[1]][i[0]]

    for i in combinations(t2, 2):
        total2 += graph[i[0]][i[1]] + graph[i[1]][i[0]]

    result = min(result, abs(total1 - total2))


print(result)