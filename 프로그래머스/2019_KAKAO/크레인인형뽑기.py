# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    board = list(map(list, zip(*board)))
    stack = [0]
    for i in moves:
        for j in range(len(board[i-1])):
            if board[i-1][j] != 0:
                if stack[-1] == board[i-1][j]:
                    answer += 1
                    stack.pop()
                else:
                    stack.append(board[i-1][j])
                    
                board[i-1][j] = 0
                break
            
    return answer * 2