from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list) # {icn: [jfk], hnd: [iad], jfk: [hnd]}
    for a, b in tickets:
        routes[a].append(b) 
    
    for key in routes.keys():
        routes[key].sort(reverse=True)
    
    path = []
    
    def dfs(port):
        while routes[port]:
            next_port = routes[port].pop()
            dfs(next_port)
        path.append(port)
        
    dfs('ICN')
    return path[::-1]