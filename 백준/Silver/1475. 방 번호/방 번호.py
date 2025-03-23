import math

n = input()
arr = [x if x not in '69' else '69' for x in str(n)]
answer = 0
dict = {}

for a in arr:
    if a in dict:
        dict[a] += 1
    else:
        dict[a] = 1

if '69' in dict.keys():
    dict['69'] = math.ceil(dict['69'] / 2)

print(sorted(dict.values(), reverse=True)[0])