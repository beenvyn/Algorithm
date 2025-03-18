import sys

input = sys.stdin.readline
n = int(input())
strings = [input()[::-1] for _ in range(n)]

for i in range(len(strings[0])):
    temp = []
    for string in strings:
        temp.append(string[:i + 1])
    if len(set(temp)) == len(temp):
        print(i)
        break
