# https://www.acmicpc.net/problem/2504

l = list(map(str, input()))

s = []
answer = 0
record = 0
for i in l:
    

    if i == ')':
        if s[-1] == '(':
            temp = s.pop()
            if s:
                answer += 2 * record
                record = 0
            else:
                record += 2
    
    elif i == ']':
        if s[-1] == '[':
            temp = s.pop()
            if s:
                answer += 2 * record
                record = 0
            else:
                record += 2

    else:
        s.append(i)

print(answer)