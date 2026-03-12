def solution(arr):
    answer = [0, 0]
    n = len(arr)
    
    # 영역의 수가 다 같은지 확인하는 함수
    # (왼쪽 위 꼭짓점, 오른쪽 아래 꼭짓점)
    def check(r1, c1, r2, c2):
        x = arr[r1][c1]
        for r in range(r1, r2):
            for c in range(c1, c2):
                if arr[r][c] != x:
                    return 2
        return x
                
    def dfs(r1, c1, r2, c2):
        res = check(r1, c1, r2, c2)
        
        if res != 2: # 압축이 되는 경우
            answer[res] += 1
            return
        
        size = r2 - r1
        half = size // 2
        
        # 압축이 안되는 경우 쪼개기
        dfs(r1, c1, r1 + half, c1 + half)
        dfs(r1, c1 + half, r1 + half, c2)
        dfs(r1 + half, c1, r2, c1 + half)
        dfs(r1 + half, c1 + half, r2, c2)
        
    dfs(0, 0, n, n)
    return answer