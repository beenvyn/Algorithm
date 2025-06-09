def solution(wallpaper):
    files_x = []
    files_y = []
    
    for r in range(len(wallpaper)):
        for c in range(len(wallpaper[0])):
            if wallpaper[r][c] == '#':
                files_x.append(r)
                files_y.append(c)
    
    files_x.sort()
    files_y.sort()
    
    return [files_x[0], files_y[0], files_x[-1] + 1, files_y[-1] + 1]