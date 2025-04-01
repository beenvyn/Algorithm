import sys
input = sys.stdin.readline

n, opt = input().split()
names = {input().rstrip() for _ in range(int(n))}

if opt == 'Y':
    print(len(names))
elif opt == 'F':
    print(len(names) // 2)
elif opt == 'O':
    print(len(names) // 3)