# https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3

def solution(n, arr1, arr2):
    answer = []
    
    for x, y in zip(arr1, arr2):
        result = str(bin(x|y))[2:].rjust(n, '0')
        result = result.replace('1', '#')
        result = result.replace('0', ' ')
        answer.append(result)
    return answer