# https://www.acmicpc.net/problem/1759

from itertools import combinations

l, c = map(int, input().split())
key = list(map(str, input().split()))
key.sort()

mo = set(['a', 'e', 'i', 'o', 'u'])
 
for i in combinations(key, l):
    t = set(i)
    if len(mo - t) != len(mo) and len(t - mo) > 1:
        print("".join(i))
