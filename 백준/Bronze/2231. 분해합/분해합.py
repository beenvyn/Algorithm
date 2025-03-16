num = int(input())

for n in range(num):
    temp = n + sum([int(x) for x in str(n)])
    if temp == num:
        print(n)
        break

else:
    print(0)