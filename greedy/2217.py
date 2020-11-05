import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
w = list(int(input()) for _ in range(n))

w.sort(reverse = True)

max = min(w) * n

for i in range(1, n + 1):
	if i * w[i-1] > max:
		max = i * w[i-1]

print(max)