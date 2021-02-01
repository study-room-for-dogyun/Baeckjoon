t = int(input())

n = [list(map(int, (input().split()))) for _ in range(t)]

def uc(a, b):
    if a < b:
        a, b = b, a
    
    while b != 0:
        a, b = b, a % b
    
    return a

for i in n:
    print(i[0] * i[1] // uc(i[0], i[1]))