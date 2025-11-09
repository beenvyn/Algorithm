def solution(dirs):
    answer = 0
    opts = {'U': (0,1), 'D': (0,-1), 'R': (1,0), 'L': (-1,0)}
    x, y = 0, 0
    visited = set()
    
    for d in dirs:
        nx, ny = x + opts[d][0], y + opts[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            cur_route = tuple(sorted(((x,y),(nx,ny))))
            if cur_route not in visited:
                answer += 1
                visited.add(cur_route)
            x, y = nx, ny
        
    return answer