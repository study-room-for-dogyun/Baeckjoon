# https://www.acmicpc.net/problem/1747

N = int(input())
MAX = 1003002
prime = [True] * MAX
prime[1] = False


def set_prime():
    for i in range(2, MAX):
        if prime[i]:
            for k in range(i + i, MAX, i):
                prime[k] = False


def check_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


set_prime()
for i in range(N, MAX):
    if prime[i] and check_palindrome(i):
        print(i)
        break
