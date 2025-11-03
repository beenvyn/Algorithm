import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

left = 0
right = N - 1
answer = nums[left] + nums[right]

while left + 1 < right:
    left_move = nums[left + 1] + nums[right]
    right_move = nums[left] + nums[right - 1]

    if abs(left_move) < abs(right_move):
        left += 1
        if abs(left_move) < abs(answer):
            answer = left_move
    else:
        right -= 1
        if abs(right_move) < abs(answer):
            answer = right_move

print(answer)