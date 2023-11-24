def solution(n, build_frame):
    
    def check_install_column(x, y):
        # 기둥이 바닥에 있는 경우
        if not y:
            return True
        # 기둥이 보의 한쪽 끝 부분 위에 있는 경우
        if (x - 1 >= 0 and arr[y][x - 1][1]) or arr[y][x][1]:
            return True
        # 기둥이 다른 기둥 위에 있는 경우
        if arr[y - 1][x][0]:
            return True
        return False
    
    
    def check_install_beam(x, y):
        # 보의 한쪽 끝 부분이 기둥 위에 있는 경우
        if arr[y - 1][x][0] or arr[y - 1][x + 1][0]:
            return True
        # 보의 양쪽 끝 부분이 모두 다른 보와 연결되어 있는 경우
        if x - 1 >= 0 and arr[y][x - 1][1] and arr[y][x + 1][1]:
            return True
        return False
    
    
    def check_remove_column(x, y):
        arr[y][x][0] = 0
        # 왼쪽 위에 보가 있는 경우
        if x - 1 >= 0 and arr[y + 1][x - 1][1] and not check_install_beam(x - 1, y + 1):
            return False
        # 오른쪽 위에 보가 있는 경우
        if arr[y + 1][x][1] and not check_install_beam(x, y + 1):
            return False
        # 위에 기둥이 있는 경우
        if arr[y + 1][x][0] and not check_install_column(x, y + 1):
            return False
        return True
        
        
    def check_remove_beam(x, y):
        arr[y][x][1] = 0
        # 양쪽 보 확인
        for i in [-1, 1]:
            nx = x + i
            if 0 <= nx < n and arr[y][nx][1] and not check_install_beam(nx, y):
                return False
        # 양쪽 기둥 확인
        for i in [0, 1]:
            nx = x + i
            if arr[y][nx][0] and not check_install_column(nx, y):
                return False
        return True
    
    
    arr = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    for command in build_frame:
        x, y, is_beam, is_installation = map(int, command)
        if is_installation:
            if not is_beam and check_install_column(x, y):
                arr[y][x][0] = 1
            elif is_beam and check_install_beam(x, y):
                arr[y][x][1] = 1
        else:
            if not is_beam and not check_remove_column(x, y):
                arr[y][x][0] = 1
            elif is_beam and not check_remove_beam(x, y):
                arr[y][x][1] = 1
    
    answer = []
    for x in range(n + 1):
        for y in range(n + 1):
            for i in range(2):
                if arr[y][x][i]:
                    answer.append([x, y, i])
            
    return answer