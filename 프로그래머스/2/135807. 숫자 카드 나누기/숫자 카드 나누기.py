from math import gcd

def solution(arrayA, arrayB):
    answer = 0
    
    def gcd_array(arr):
        g = arr[0]
        for x in arr[1:]:
            g = gcd(g, x)
        return g
    
    def check(arr, num):
        for x in arr:
            if x % num == 0:
                return False
        return True        
    
    gcd_a, gcd_b = gcd_array(arrayA), gcd_array(arrayB)
    
    if check(arrayB, gcd_a):
        answer = max(answer, gcd_a)
    
    if check(arrayA, gcd_b):
        answer = max(answer, gcd_b)
        
    return answer