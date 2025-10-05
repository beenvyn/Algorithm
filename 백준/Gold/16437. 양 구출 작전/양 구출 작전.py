import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

n = int(input())
infos = [input().split() for _ in range(n - 1)]

tree = {} # {1: [2,3,4], 2:[5,6], 6: [7] }

for idx, info in enumerate(infos):
    parent = int(info[2])
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(idx + 2)


def dfs(node):
    # node 섬에서 1번 섬 방향으로 살아서 올라오는 양의 수
    sheep = 0
    
    # 1) 자식들에서 올라오는 양 합치기
    for child in tree.get(node, []):
        sheep += dfs(child)
    
    # 2) 현재 섬의 동물 반영
    if node != 1:
        opt, cnt = infos[node-2][0], int(infos[node-2][1]) 
    
        if opt == 'S':
            sheep += cnt
        else:
            sheep = max(0, sheep - cnt)
    
    return sheep

print(dfs(1))