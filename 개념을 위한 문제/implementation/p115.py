# 책 115쪽

n = input()

x = int(n[1])
y = int(ord(n[0]) - ord('a')) + 1
count = 0

move = [(-2, -1), (2, -1), (-1, -2), (1, -2), (-2, 1), (2, 1), (-1, 2), (1, 2)]

for i in move:
    dx = x + i[0]
    dy = y + i[1]

    if dx < 1 or dx > 8 or dy < 1 or dy > 8:
        continue

    count += 1

print(count)