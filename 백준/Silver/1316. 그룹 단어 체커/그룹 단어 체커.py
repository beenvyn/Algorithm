from collections import Counter

n = int(input())
answer = 0

for i in range(n):
    word = input()
    word_count = Counter(word)

    for char, cnt in word_count.items():
        if cnt > 1:
            if char * cnt not in word:
                break
    
    else:
        answer += 1
      
print(answer)