n = int(input())

answer = 0
for num in range(1, n + 1):
    str_num = str(num)
    if len(str_num) <= 2:
        answer += 1
    else:
        d = int(str_num[0]) - int(str_num[1])
        for j in range(1, len(str_num) - 1):
            if int(str_num[j]) - int(str_num[j + 1]) != d:
                break
        else:
            answer += 1
        
print(answer)