n = int(input())
string = input()

b = string.replace('R', ' ').split()
r = string.replace('B', ' ').split()

print(min(len(b), len(r)) + 1)