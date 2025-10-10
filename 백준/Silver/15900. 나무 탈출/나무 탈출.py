import sys
sys.setrecursionlimit(500000)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
total = 0

def dfs(node, depth):
    global total
    visited[node] = True
    has_child = False
    
    for adj in graph[node]:
        if not visited[adj]:
            dfs(adj, depth+1)
            has_child = True
        
    if not has_child:
        total += depth

dfs(1,0)  

print('Yes') if total % 2 else print('No')