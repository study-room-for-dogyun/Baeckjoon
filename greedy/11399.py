n = int(input())
p = list(map(int, input().split()))
p.sort()

result = 0
for i in range(n):
	result += (n - i) * p[i]

print(result)