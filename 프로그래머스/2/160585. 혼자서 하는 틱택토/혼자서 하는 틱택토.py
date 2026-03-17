def solution(board):
    def check_win(target):
        # 가로
        for r in range(3):
            if board[r][0] == board[r][1] == board[r][2] == target:
                return True
        
        # 세로
        for c in range(3):
            if board[0][c] == board[1][c] == board[2][c] == target:
                return True
        
        # 대각선
        if board[0][0] == board[1][1] == board[2][2] == target or board[0][2] == board[1][1] == board[2][0] == target:
            return True
        
        return False
        
    o_cnt, x_cnt = 0, 0
    for row in board:
        o_cnt += row.count('O')
        x_cnt += row.count('X')
        
    # X가 더 많거나, O가 2개 이상 더 많으면 불가능
    if x_cnt > o_cnt or o_cnt - x_cnt >= 2:
        return 0
        
    o_win = check_win('O')
    x_win = check_win('X')

    # O가 이겼으면 O가 한 개 더 많아야 함
    if o_win and o_cnt != x_cnt + 1:
        return 0
    
    # X가 이겼으면 O와 X 개수가 같아야 함
    if x_win and o_cnt != x_cnt:
        return 0
        
    return 1