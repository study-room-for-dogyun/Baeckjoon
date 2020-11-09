n = int(input())

def fibo(x):
    cur, prev = 1, 1

    for i in range(3, n+1):
        cur, prev = prev + cur, cur
    
    return cur

print(fibo(n))