N = int(input())
board = tuple(tuple(map(int,tuple(input()))) for _ in range(N))
def dfs(Sx, Ex, Sy, Ey):
    if Ex-Sx > 2:
        midx = (Sx+Ex)//2
        midy = (Sy+Ey)//2
        a = dfs(Sx, midx, Sy, midy)
        b = dfs(midx, Ex, Sy, midy)
        c = dfs(Sx, midx, midy, Ey)
        d = dfs(midx, Ex, midy, Ey)
        target = a+b+c+d
        if len(target) == 4 and target.count('1') == 4:
            return '1'
        elif len(target) == 4 and target.count('0') == 4:
            return '0'
        else:
            return '('+a+b+c+d+')'
    elif Ex-Sx < 2:
        return str(board[Sx][Sy])
    else:
        cnt = 0
        shape = '('
        for i in range(Sy, Ey):
            for j in range(Sx, Ex):
                if board[i][j]:
                    cnt += 1
                    shape += '1'
                else:
                    shape += '0'
        if cnt == 4 or cnt == 0:
            return '1' if cnt else '0'
        else:
            return shape + ')'
print(dfs(0, N, 0, N))

