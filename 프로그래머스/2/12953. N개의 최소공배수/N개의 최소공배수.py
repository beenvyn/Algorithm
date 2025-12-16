import math

def solution(arr):
    if len(arr) > 1:
        answer = (arr[0] * arr[1]) // math.gcd(arr[0], arr[1])
    else:
        return arr[0]
    
    for i in range(2, len(arr)):
        answer *= arr[i] // math.gcd(answer, arr[i])
    
    return answer