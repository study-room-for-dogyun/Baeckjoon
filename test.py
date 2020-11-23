n = int(input())

def fibo(x):
    prev, cur = 0, 1
    for _ in range(2, x + 1):
        prev, cur = cur, prev + cur
    
    return cur

print(fibo(n))