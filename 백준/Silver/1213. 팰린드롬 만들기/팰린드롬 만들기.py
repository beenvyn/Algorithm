from collections import Counter

string = input();
counter = Counter(string);
answer = ''
mid = '';
cnt = 0

for k, v in list(counter.items()):
    if v % 2:
        cnt += 1
        mid = k
        if cnt > 1:
            print("I'm Sorry Hansoo")
            exit()

for k, v in sorted(counter.items()):
    answer += k * (v // 2)

print(answer + mid + answer[::-1])