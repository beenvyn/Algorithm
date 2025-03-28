import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    sound = input().rstrip().split()

    while True:
        opts = input().split()

        if '?' in opts[-1]:
            print(*sound)
            break

        while opts[-1] in sound:
            sound.remove(opts[-1])