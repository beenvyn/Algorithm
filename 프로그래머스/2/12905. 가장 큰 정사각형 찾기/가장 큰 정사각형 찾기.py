
def solution(board):
    answer = 0

    rows, cols = len(board), len(board[0])
    
    for r in range(1, rows):
        for c in range(1, cols):
            if board[r][c] == 1:
                board[r][c] = min(board[r-1][c-1], board[r-1][c], board[r][c-1]) + 1

    return max(map(max, board))**2