def solution(s):
    arr = list(map(int,s.split()))
    return ' '.join(map(str,[min(arr), max(arr)]))