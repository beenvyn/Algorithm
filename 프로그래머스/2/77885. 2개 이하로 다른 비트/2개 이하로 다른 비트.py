def solution(numbers):
    answer = []
            
    for x in numbers:
        # 짝수면 마지막 비트만 0 -> 1로 바꾸면 끝
        if x % 2 == 0:
            answer.append(x + 1)
        else:
            # 가장 오른쪽에 있는 0을 1로 바꾸기
            # 그 다음 위치의 1을 0으로 바꾸기
            bit = '0' + bin(x)[2:] # 맨 앞에 0 하나 붙이기
            idx = bit.rfind('0')
            
            bit = bit[:idx] + '10' + bit[idx+2:]
            answer.append(int(bit, 2))

    return answer