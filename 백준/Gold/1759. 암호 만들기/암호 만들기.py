import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

L, C = map(int, input().split())
chars = input().split()
chars.sort() # 사전순 암호 추출을 위해 

# 다음에 볼 문자 인덱스, 모음 개수, 현재 문자열
def dfs(idx, v_cnt, cur):
    if len(cur) == L:
        if 1 <= v_cnt <= L - 2:
            print(cur)
        return

    for i in range(idx, C):
        next_v_cnt = v_cnt + (chars[i] in ['a', 'e', 'i', 'o', 'u']) # 복구가 가능하게
        dfs(i + 1, next_v_cnt, cur + chars[i])

dfs(0, 0, '')