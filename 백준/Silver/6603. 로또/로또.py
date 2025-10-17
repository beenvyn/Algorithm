import sys
input = sys.stdin.readline

while True:
    input_arr = list(map(int, input().split()))
    k = input_arr[0]

    if k == 0:
        break

    nums_arr = input_arr[1:]
    answer = []

    def backtrack(comb, idx):
        if len(comb) == 6:
            answer.append(comb[:])
        
        for i in range(idx,k):
            comb.append(nums_arr[i])
            backtrack(comb,i+1)
            comb.pop()

    backtrack([], 0)

    for a in answer:
        print(' '.join(map(str,a)))
    print()