def solution(board, moves):
    answer = 0
    rows = list()

    for i in range(len(moves)):
        for j in range(len(board[0])):
            if board[j][moves[i] - 1] == 0:
                pass
            else:
                rows.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                break
        if len(rows) >= 2:
            if rows[-2] == rows[-1]:
                answer += 2
                del rows[-2]
                del rows[-1]
    return answer



board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]	
print(solution(board, moves))