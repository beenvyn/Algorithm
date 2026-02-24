def solution(n):
    fb = [0] * (n + 1)
    fb[1] = 1
    
    for i in range(2, n + 1):
        fb[i] = fb[i-1] + fb[i-2]
        
    return fb[n] % 1234567