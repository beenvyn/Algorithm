import sys
input = sys.stdin.readline

while True:
    try:
        s, t = input().split()
        prior = -1

        for char in s:
            idx = t.find(char, prior + 1) 

            if idx == -1:
                print('No')
                break

            prior = idx

        else:
            print('Yes')
            
    except:
        break