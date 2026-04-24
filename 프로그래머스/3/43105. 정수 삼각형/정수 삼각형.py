def solution(triangle):
    n = len(triangle)
    
    for r in range(1, n):
        for c in range(r + 1):
            left = triangle[r - 1][c - 1] if c > 0 else 0
            right = triangle[r - 1][c] if c < r else 0
            triangle[r][c] += max(left, right)

    return max(triangle[n - 1])