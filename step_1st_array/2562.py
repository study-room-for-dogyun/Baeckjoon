n = [int(input()) for _ in range(9)]


ma = 0

for i in range(len(n)):
    if n[i] == max(n):
        ma = i

print(max(n))
print(ma + 1)
