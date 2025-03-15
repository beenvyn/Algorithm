n, k = map(int, input().split())

arr = list(range(1, n + 1))
answer = []
index = 0

while arr:
    index = (index + k - 1) % len(arr)
    answer.append(arr.pop(index))
    
print('<' + ', '.join(map(str, answer)) + '>')