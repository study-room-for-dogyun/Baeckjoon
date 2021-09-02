# https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3

from itertools import combinations

def solution(nums):
    answer = 0
    
    
    for num in combinations(nums, 3):
        check = True
        num = sum(num)
        
        for i in range(2, int(num**(1/2))+1):
            if num % i == 0:
                check = False
                break
                    
        if check:
            answer += 1

    return answer