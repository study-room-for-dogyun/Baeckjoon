# 최대 공약수와 최소 공배수

n, m = map(int, input().split())

# 최대 공약수
def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


# 최소 공배수
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(n, m))
print(lcm(n, m))