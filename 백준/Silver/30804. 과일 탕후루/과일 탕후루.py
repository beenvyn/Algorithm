import sys

input = sys.stdin.readline

N = int(input())
fruits = list(map(int, input().split()))

left = 0
fruit_dict = {}
answer = 0

for right in range(N):
    current_fruit = fruits[right]

    if current_fruit in fruit_dict:
        fruit_dict[current_fruit] += 1
    else:
        fruit_dict[current_fruit] = 1
    
    while len(fruit_dict) > 2:
        fruit_to_remove = fruits[left]

        fruit_dict[fruit_to_remove] -= 1
        if fruit_dict[fruit_to_remove] == 0:
            del fruit_dict[fruit_to_remove]
        
        left += 1
    
    answer = max(answer,right-left+1)

print(answer)