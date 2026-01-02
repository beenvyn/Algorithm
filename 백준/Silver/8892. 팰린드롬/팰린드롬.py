import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]
    found = False

    for i in range(k - 1):
        if found:
            break
        for j in range(i + 1, k):
            if found:
                break
            new_words = [words[i] + words[j], words[j] + words[i]]

            for new_word in new_words:
                if new_word == new_word[::-1]:
                    print(new_word)
                    found = True
                    break
              
    if not found:
        print(0)