n = int(input())

memo = [0] * (n + 1)

def fibo(x):
    if x < 3:
        return 1

    if memo[x] != 0:
        return memo[x]
    
    memo[x] = fibo(x-1) + fibo(x-2)
    return memo[x]
    
print(fibo(n))