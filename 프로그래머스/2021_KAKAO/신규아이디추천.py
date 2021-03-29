import re

def solution(new_id):
    answer = ''
    
    answer = new_id.lower()
    answer = re.sub('[^a-z0-9-_.]', '', str(answer))
    answer = re.sub('[.]+', '.', str(answer))
    
    if answer[0] == '.':
        answer = str(answer[1:])
    
    if len(answer) >= 2:
        if answer[-1] == '.':
            answer = str(answer[:-1])
        
    if len(answer) == 0:
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[:15]
    
        if answer[-1] == '.':
            answer = answer[:-1]
    
    if len(answer) <= 2:
        lastw = answer[-1]
        while len(answer) < 3:
            answer += lastw
    
    
    print(answer)
    return answer