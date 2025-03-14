n = int(input())

arr = [input() for _ in range(n)]
answer = sorted(arr, key=lambda x:(len(x), sum([int(num) for num in x if num.isdigit()]), x))

for a in answer:
    print(a)