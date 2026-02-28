def solution(k, ranges):
    answer = []
    dots = [k]
    x = 0
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        x += 1
        dots.append(k)
    
    n = len(dots) - 1
    for a, b in ranges:
        total = 0
        if a > n + b:
            answer.append(-1)
            continue
        for i in range(a, n + b):
            h = dots[i] + dots[i + 1]
            total += h / 2
        answer.append(total)
            
    return answer