import math

def solution(w,h):
    g = math.gcd(w, h)
    unusable = w // g + h // g - 1

    return w * h - (unusable * g)