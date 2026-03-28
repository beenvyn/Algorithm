def solution(brown, yellow):
    for i in range(1, int(yellow**0.5) + 1):
        if yellow % i == 0:
            a = yellow // i
            b = i
            
            if a + b + 2 == brown // 2:
                return [a + 2, b + 2]