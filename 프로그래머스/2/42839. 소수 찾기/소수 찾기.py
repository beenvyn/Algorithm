def solution(numbers):
    n = len(numbers)
    answer = set()
    
    def isPrime(num):
        if num < 2:
            return False
        for x in range(2, int(num**0.5) + 1):
            if num % x == 0:
                return False
        return True
    
    def backtrack(cur, visited):
        if cur:
            num = int(cur)
            if isPrime(num):
                answer.add(num)
        
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                backtrack(cur + numbers[i], visited)
                visited[i] = False
    
    visited = [False] * (n)
    backtrack('', visited)

    return len(list(answer))