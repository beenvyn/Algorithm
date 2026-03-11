def solution(rows, cols, queries):
    answer = []

    board = [[0] * cols for _ in range(rows)]
    num = 1
    for r in range(rows):
        for c in range(cols):
            board[r][c] = num
            num += 1
    
    for r1, c1, r2, c2 in queries:
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1
        
        prev = board[r1][c1]
        min_val = prev
        
        # 위 행(왼 -> 오)
        for c in range(c1 + 1, c2 + 1):
            board[r1][c], prev = prev, board[r1][c]
            min_val = min(min_val, prev)
        
        # 오른쪽 열(위 -> 아래)
        for r in range(r1 + 1, r2 + 1):
            board[r][c2], prev = prev, board[r][c2]
            min_val = min(min_val, prev)
        
        # 아래 행(오 -> 왼)
        for c in range(c2 - 1, c1 - 1, -1):
            board[r2][c], prev = prev, board[r2][c]
            min_val = min(min_val, prev)
        
        # 왼쪽 열(아래 -> 위)
        for r in range(r2 - 1, r1 - 1, -1):
            board[r][c1], prev = prev, board[r][c1]
            min_val = min(min_val, prev)
        
        answer.append(min_val)
        
    return answer