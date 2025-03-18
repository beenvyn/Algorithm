m, n = map(int, input().split())

dict = {'0': 'zero', '1':'one', '2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight', '9':'nine'}
arr = []

for x in range(m, n + 1):
    temp = ''
    for i in range(len(str(x))):
        temp += dict[str(x)[i]] + ' '
    arr.append(temp)

sorted_arr = sorted(arr)
cnt = 0

for a in sorted_arr:
    print(arr.index(a) + m, end=' ')
    cnt += 1
    if cnt % 10 == 0:
        print()