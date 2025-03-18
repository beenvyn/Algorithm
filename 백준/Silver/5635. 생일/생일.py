n = int(input())
list = [input().split() for _ in range(n)]
sorted_list = sorted(list, key=lambda x:(int(x[3]),int(x[2]),int(x[1])) )

print(sorted_list[-1][0])
print(sorted_list[0][0])