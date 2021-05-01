# https://programmers.co.kr/learn/courses/30/lessons/67256#

def solution(numbers, hand):
    answer = ''
    
    left = [3, 0]
    right = [3, 2]
    
    for i in numbers:
        if i % 3 == 1:              # 왼쪽 라인 숫자
            answer += 'L'
            left = [i//3, 0]
        
        elif i % 3 == 0 and i != 0: # 오른쪽 라인 숫자
            answer += 'R'
            right = [(i//3)-1, 2]
        
        else:
            if i == 0:
                mid = [3, 1]
            else:
                mid = [i//3, 1]
            
            dis_l = abs(left[0]  - mid[0]) + abs(left[1] - mid[1])
            dis_r = abs(right[0] - mid[0]) + abs(right[1] - mid[1])
            # dis_l = (pow(left[0] - mid[0], 2) + pow(left[1] - mid[1], 2))**0.5
            # dis_r = (pow(right[0] - mid[0], 2) + pow(right[1] - mid[1], 2))**0.5

            if dis_l > dis_r:
                right = [mid[0], mid[1]]
                answer += 'R' 
            elif dis_l < dis_r:
                left = [mid[0], mid[1]]
                answer += 'L' 
            else:
                if hand == 'left':
                    left = [mid[0], mid[1]]
                    answer += 'L' 
                else:
                    right = [mid[0], mid[1]]
                    answer += 'R' 
                
                
    return answer