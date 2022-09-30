def solution(board, moves):
    answer = 0
    stk = []
    result = []
    for j in range(len(board[0])):
        stk2 = []
        for i in range(len(board)) :
            stk2.append(board[i][j])
        stk.append(stk2[::-1])
            
            
    for i in moves:
        for j in range(len(stk[i-1])-1,-1,-1):
            if stk[i-1][j] != 0: 
                result.append(stk[i-1][j])
                stk[i-1][j] = 0
                break
        
        if len(result) >1 :
            if result[-1] == result[-2]:
                result.pop()
                result.pop()
                answer += 2
                
    return answer