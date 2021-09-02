# https://www.acmicpc.net/problem/14226
from collections import deque

# s = int(input())
c = [list(map(int, input().split())) for _ in range(999)]

def bfs(s):
    # [이모티콘 개수, 현재 횟수, 복사 여부, 클립보드의 개수]
    q = deque([[1, 0, False, 0]])
    visited = {}

    while q:

        num, cnt, copy, clip = q.popleft()

        # print(num, cnt, copy, clip)
        # print(visited)

        if num == s:
            return cnt
        
        if num > 1000:
            continue

        if num in visited:
            if visited[num] == 1:
                continue

        cnt += 1
        q.append([num, cnt, True, num])                 # 1. 복사하기  

        if copy:    # 클립보드에 복사한 게 없으면
            q.append([num+clip, cnt, copy, clip])       # 2. 붙여넣기   

        if num > 0:     # 이모티콘 삭제할 게 있을 때
            q.append([num-1, cnt, copy, clip])          # 3. 삭제하기

        if num in visited:
            visited[num] += 1
        else:
            visited[num] = 1

for i in c:
    result = bfs(i[0])
    if result == i[1]:
        print(True, i, result)
    else:
        print(False, i, result)

# print(bfs())
# print(visited)
