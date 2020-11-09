import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
array = sorted(list(map(int, input().split())))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in array:
        if i > mid:
            total += i - mid
    
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)


# 파라메트릭 서치 문제 : 재귀가 아닌 반복문으로