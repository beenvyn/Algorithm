n = int(input())
arr = [input().split() for _ in range(n)]
arr.append([0, '48:00'])
score1, score2 = 0, 0
time1, time2 = 0, 0


# MM:SS -> 초 단위로 변경
def time_to_seconds(time):
    m = int(time.split(':')[0])
    s = int(time.split(':')[1])
    return m * 60 + s

# 초 단위 -> MM:SS로 변경
def seconds_to_time(seconds):
    m = seconds // 60
    s = seconds % 60
    return str(m).rjust(2, '0') + ':' + str(s).rjust(2, '0')

for i in range(n):
    cur_team, cur_time = arr[i]
    next_time = arr[i + 1][1]

    if cur_team == '1':
        score1 += 1
    elif cur_team == '2':
        score2 += 1
    if score1 > score2:
        time1 += time_to_seconds(next_time) - time_to_seconds(cur_time)
    elif score1 < score2:
        time2 += time_to_seconds(next_time) - time_to_seconds(cur_time)

print(seconds_to_time(time1))
print(seconds_to_time(time2))
