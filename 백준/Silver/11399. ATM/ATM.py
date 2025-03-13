n = input()
p = input()
times = [int(x) for x in p.split()]

def cal(times):
    answer = []
    times = sorted(times)
    temp = 0

    for time in times:
        temp += time
        answer.append(temp)
    return sum(answer)

print(cal(times))