row, col = map(int, input().split())
board = []
start_w = ['W','B','W','B','W','B','W','B']
start_b = ['B','W','B','W','B','W','B','W']
min = 1000000
for i in range(row):
    board.append(list(input()))

    
def board_8x8(row,col, board):
    board_tmp = []
    cnt_w = 0
    cnt_b = 0
    for i in range(8):
        board_tmp.append(board[i+row][0+col:8+col]) 
        
    # W로 시작할때
    for i in range(0,8,2):
        for j in range(8):
            if board_tmp[i][j]!= start_w[j]:
                cnt_w +=1
    for i in range(1,8,2):
        for j in range(8):
            if board_tmp[i][j]!= start_b[j]:
                cnt_w +=1

    # B로 시작할때
    for i in range(0,8,2):
        for j in range(8):
            if board_tmp[i][j]!= start_b[j]:
                cnt_b +=1
    for i in range(1,8,2):
        for j in range(8):
            if board_tmp[i][j]!= start_w[j]:
                cnt_b +=1
    
    if cnt_w <= cnt_b:
        return cnt_w
    else : 
        return cnt_b

    
for i in range(row-7):
    for j in range(col-7): 
        tmp = board_8x8(i,j,board)
        if tmp < min:
            min = tmp

print(min)