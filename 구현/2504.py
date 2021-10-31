# https://www.acmicpc.net/problem/2504

data = list(map(str, input()))

stack = []
answer = 0
for i in data:

    if i == '(' or i == '[':
        stack.append(i)
        continue


    if i == ']':
        if stack[-1] == '[':
            stack.pop()
            stack.append(3)
        
        elif stack[-1] == int:
            pass

    elif i == ')':
        if stack[-1] == '(':
            stack.pop()
            stack.append(2)

    
print(stack)    

if stack:
    print(0)
else:
    print(answer)