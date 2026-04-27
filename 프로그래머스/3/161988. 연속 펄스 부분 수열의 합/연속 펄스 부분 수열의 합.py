def solution(sequence):
    n = len(sequence)
    
    def get_max(num):
        arr = []
        
        for s in sequence:
            arr.append(s * num)
            num *= -1
        
        dp = [0] * n  # dp[i]: i번째 원소를 마지막으로 하는 연속 수열의 최대 합
        dp[0] = arr[0]
        
        for i in range(1, n):
            dp[i] = max(arr[i], dp[i - 1] + arr[i])
        
        return max(dp)
    
    return max(get_max(1), get_max(-1))