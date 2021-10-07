# https://www.acmicpc.net/problem/15717
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
print(pow(2, (n-1), 1000000007) if n != 0 else 1)