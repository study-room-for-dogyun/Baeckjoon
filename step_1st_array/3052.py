n = [int(input()) for _ in range(10)]
x = [n[i]%42 for i in range(10)]

temp = []
count = 0

for i in x:
    if i not in temp:
        temp.append(i)
        count += 1
print(count)