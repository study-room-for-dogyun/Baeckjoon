# https://www.acmicpc.net/problem/17140

r, c, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]
ans = 0

def rearrange(l):

    cnt = {}
    for i in l:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1

    cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)    
    
    result = []
    for a, b in cnt:
        result.append(a)
        result.append(b)
    
    print(result)
rearrange([3, 1, 1])

for i in range(100):

    if graph[r-1][c-1] == k:
        ans = i
        break

    len_r = len(graph)
    len_c = len(graph[0])

    # if len_r >= len_c:


    
    # if len_r < len_c:

    
print(ans)