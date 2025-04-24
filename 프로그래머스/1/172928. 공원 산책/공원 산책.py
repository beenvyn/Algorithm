def solution(park, routes):
    answer = []
    options = {'N': [-1, 0], 'E':[0, 1], 'S':[1, 0], 'W':[0, -1]}
    h = len(park)
    w = len(park[0])
    blocked = []
    cur_y, cur_x = 0, 0
    
    for y in range(h):
        for x in range(w):
            if park[y][x] == 'S':
                cur_x, cur_y = x, y
            elif park[y][x] == 'X':
                blocked.append([y, x])

    for route in routes:
        op, n = route.split()
        n = int(n)
        ny, nx = cur_y, cur_x
        valid = True

        for _ in range(n):
            ny += options[op][0]
            nx += options[op][1]
            
            if not (0 <= nx < w and 0 <= ny < h) or [ny, nx] in blocked:
                valid = False
                break
            
        if valid:
            cur_y, cur_x = ny, nx
            
    return [cur_y, cur_x]