# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''
    
    p = {}
    for i in participant:
        if i in p:
            p[i] += 1
        else:
            p[i] = 1

    c = {}
    for i in completion:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1

    for i in participant:
        if i not in c:
            return i
        if c[i] != p[i]:
            return i