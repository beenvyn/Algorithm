def solution(N, number):
    dp = [set() for _ in range(9)]  # dp[k]: N을 k번 써서 표현할 수 있는 수의 집합
    
    for k in range(1,9):
        concat = int(str(N) * k)
        dp[k].add(concat)
        if concat == number:
            return k
    
        for i in range(1,k):
            for a in dp[i]:
                for b in dp[k-i]:
                    dp[k].add(a+b)
                    dp[k].add(a-b)
                    dp[k].add(a*b)
                    if b != 0:
                        dp[k].add(a//b)
            
            if number in dp[k]:
                return k
                
    return -1