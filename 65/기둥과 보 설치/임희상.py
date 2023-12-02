def solution(n, build_frame):
    
    def install_column(y, x):
        if not x:
            return True
        if (y - 1 >= 0 and board[x][y - 1][1]) or board[x][y][1]:
            return True
        if board[x - 1][y][0]:
            return True
        return False
    
    def install_beam(y, x):
        if board[x - 1][y][0] or board[x - 1][y + 1][0]:
            return True
        if y - 1 >= 0 and board[x][y - 1][1] and board[x][y + 1][1]:
            return True
        return False
    
    def remove_column(y, x):
        board[x][y][0] = 0
        if y - 1 >= 0 and board[x + 1][y - 1][1] and not install_beam(y - 1, x + 1):
            return False
        if board[x + 1][y][1] and not install_beam(y, x + 1):
            return False
        if board[x + 1][y][0] and not install_column(y, x + 1):
            return False
        return True
        
    def remove_beam(y, x):
        board[x][y][1] = 0
        for i in [-1, 1]:
            ny = y + i
            if 0 <= ny < n and board[x][ny][1] and not install_beam(ny, x):
                return False
        for i in [0, 1]:
            ny = y + i
            if board[x][ny][0] and not install_column(ny, x):
                return False
        return True
    
    board = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    for command in build_frame:
        y, x, is_beam, is_installation = map(int, command)
        if is_installation:
            if not is_beam and install_column(y, x):
                board[x][y][0] = 1
            elif is_beam and install_beam(y, x):
                board[x][y][1] = 1
        else:
            if not is_beam and not remove_column(y, x):
                board[x][y][0] = 1
            elif is_beam and not remove_beam(y, x):
                board[x][y][1] = 1
    
    answer = []
    for y in range(n + 1):
        for x in range(n + 1):
            for i in range(2):
                if board[x][y][i]:
                    answer.append([y, x, i])
            
    return answer
