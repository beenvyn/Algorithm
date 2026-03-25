import math

def solution(arr):
    lcm = arr[0]
    
    # 최소 공배수는 쌍 단위로 계산해야 함
    for a in arr[1:]:
        lcm = lcm * a // math.gcd(lcm, a)
    
    return lcm