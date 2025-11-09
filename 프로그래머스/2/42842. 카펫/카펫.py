def solution(brown, yellow):
    max_num = max(2,int(yellow // 2) + 1)
    for i in range(1, max_num):
        if yellow % i == 0:
            y, x = i, yellow // i
            total = x * 2 + y * 2 + 4
            if total == brown:
                return [x + 2, y + 2]
