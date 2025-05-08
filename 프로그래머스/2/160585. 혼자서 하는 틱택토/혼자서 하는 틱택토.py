def check_win(board, player):
    # 가로 확인
    for row in board:
        if all(each == player for each in row):
            return True
    
    # 세로 확인
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # 대각선 확인
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def solution(board):
    # 개수 확인
    count_O = sum(row.count('O') for row in board)
    count_X = sum(row.count('X') for row in board)
    
    # X의 개수가 O의 개수랑 똑같은 경우 or 0의 개수가 x의 개수보다 하나 많은 경우가 아니면 다 비정상
    if not(count_O == count_X or count_O == count_X + 1):
        return 0
    
    # 이겼는지 확인
    X_wins = check_win(board, 'X')
    O_wins = check_win(board, 'O')
    
    if O_wins and count_O != count_X + 1:
        return 0
    if X_wins and count_O != count_X:
        return 0
    
    return 1