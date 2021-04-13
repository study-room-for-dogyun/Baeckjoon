# https://www.acmicpc.net/problem/11723

m = int(input())
oper = [list(map(str, input().split())) for _ in range(m)]

s = 0
while oper:
    if len(oper[0]) == 2:
        a, x = oper[0][0], int(oper[0][1])
    else:
        a = oper[0][0]
    del oper[0]

    
    if a == 'add':
        if s & (1 << x-1) == 0:
            s |= (1 << x-1)
    
    elif a == 'remove':
        if s & (1 << x-1) == 1:
            s |= 
            
    elif a == 'check':
        if check[x]:
            print(1)
        else:
            print(0)
    
    elif a == 'toggle':
        
    elif a == 'all':
        s = 0xfffff
    else:
        s = 0