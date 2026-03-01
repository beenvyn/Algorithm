import math

def solution(w,h):
    # 각 블록마다 잘리는 칸 수: 가로 + 세로 - 1 (a + b - 1)
    # a는 w를 최소 공약수로 나눈 값, b는 h를 최소 공약수로 나눈 값이고 이게 최소 공약수 번 반복되므로 
    # (w/g + h/g - 1) * g
    unusable = w + h - math.gcd(w, h)
    return w * h - unusable