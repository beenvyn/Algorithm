t = int(input())

for _ in range(t):
    j, n = map(int, input().split())
    
    answer = 0
    boxes = []
    for i in range(n):
        a, b = map(int, input().split())
        boxes.append(a * b)

    for box in sorted(boxes, reverse=True):
        if j <= 0:
            print(answer)
            break
        j -= box
        answer += 1