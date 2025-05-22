def solution(info, edges):
    n = len(info)
    visited = [False] * n
    visited[0] = True  # 0번 노드(양)부터 시작

    def dfs(sheep, wolf):
        if sheep == wolf:  # 늑대 수가 양 수와 같아지면 종료
            return sheep

        max_sheep = sheep

        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = True  # 방문 처리

                if info[child] == 0:  # 양
                    max_sheep = max(max_sheep, dfs(sheep + 1, wolf))
                else:  # 늑대
                    max_sheep = max(max_sheep, dfs(sheep, wolf + 1))

                visited[child] = False  # 백트래킹

        return max_sheep

    return dfs(1, 0)  # 0번 노드가 양이므로 시작 sheep=1, wolf=0
