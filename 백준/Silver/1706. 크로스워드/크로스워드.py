import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
board = [input().strip() for _ in range(rows)]

words = []
# 길이가 2 이상이어야 함
# 가로 확인
for r in range(rows):
    word = ''
    for c in range(cols):
        if board[r][c] != '#':
            word += board[r][c]
        else:
            if len(word) > 1:
                words.append(word)
            word = ''
    if len(word) > 1:
        words.append(word)

# 세로 확인
for c in range(cols):
    word = ''
    for r in range(rows):
        if board[r][c] != '#':
            word += board[r][c]
        else:
            if len(word) > 1:
                words.append(word)
            word = ''
    if len(word) > 1:
        words.append(word)

words.sort()
print(words[0])