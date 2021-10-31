# https://www.acmicpc.net/problem/1541

n = input().split('-')

result = 0

temp = list(map(int, n[0].split('+')))
result += sum(temp)

for i in n[1:]:
	temp = list(map(int, i.split('+')))
	result -= sum(temp)

print(result)