def solution(number, k):
    stack = []
    
    for num in str(number):
        # 현재 숫자와 비교하여, 앞에 있는 숫자가 더 작다면 제거(pop)
        while k > 0 and stack and stack[-1] < int(num):
            stack.pop()
            k -= 1
        stack.append(int(num))
    
    # 아직 k가 남아 있다면 (이미 내림차순이어서 pop이 덜 되었을 경우)
    # 뒤에서 k개를 잘라냄 → 뒤쪽을 제거하는 것이 최댓값 유지에 유리
    if k > 0:
        stack = stack[:-k]

    return ''.join(map(str,stack))