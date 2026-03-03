def solution(n):
    answer = 0
    cols = [] # cols[r] = c : r행 c열에 퀸이 있음
    
    def backtrack(row):
        nonlocal answer
        
        if row == n:
            answer += 1
            return
        
        for col in range(n):
            # 열 충돌 검사
            if col in cols:
                continue
            
            # 대각선 충돌 검사
            # 새로 놓으려는 위치(row, col)와 기존에 놓인 위치(r, cols[r])의 열 차이와 행 차이가 같으면 둘이 대각선에 위치한다는 뜻
            if any(abs(row - r) == abs(col - cols[r]) for r in range(row)):
                continue
            
            cols.append(col)
            backtrack(row + 1)
            cols.pop()
    
    backtrack(0)
    return answer