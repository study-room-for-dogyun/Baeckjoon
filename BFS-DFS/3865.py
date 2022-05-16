# https://www.acmicpc.net/problem/3865

from collections import deque

while True:

    # INPUT
    n = int(input())
    if n == 0: 
        break

    dic = {}
    for _ in range(n):
        society, members = input().split(':')
        dic[society] = members[:-1].split(',')


    # Solution
    first = list(dic.keys())[0]
    for member in dic[first]:
        if member in dic:        # member가 society이면
            for i in dic[member]:
                if i not in dic[first]:
                    dic[first].append(i)


    # OUTPUT
    answer = 0
    for i in dic[first]:
        if i not in dic:        
            answer += 1

    print(answer)