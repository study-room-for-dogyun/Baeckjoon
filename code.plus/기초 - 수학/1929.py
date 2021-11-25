# https://www.acmicpc.net/problem/1929

N, M = map(int, input().split())

prime = [True] * (M + 1)

# 에라토스테네스의 체로 소수 구하기
prime[0], prime[1] = False, False
for num in range(2, len(prime)):
    if prime[num]:
        for i in range(2*num, len(prime), num):
            prime[i] = False

for idx, is_prime in enumerate(prime):
    if is_prime and idx >= N:
        print(idx)
