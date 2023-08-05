dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
target = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 'X':
            count = 0
            for k in range(4):
                x = i+dx[k]
                y = j+dy[k]
                if 0 <= x < R and 0 <= y < C:
                    if board[x][y] == '.':
                        count += 1
                else:
                    count += 1
            if count >= 3:
                target.append([i, j])
for x, y in target:
    board[x][y] = '.'
x0, y0 = 0, C-1
x1, y1 = 0, 0
for i in range(R):
    if 'X' in board[i]:
        x0 = i
        break
for i in range(R-1, -1, -1):
    if 'X' in board[i]:
        x1 = i
        break
for i in range(x0, x1+1):
    for j in range(C):
        if board[i][j] == 'X':
            y0 = min(y0, j)
            y1 = max(y1, j)
for i in range(x0, x1+1):
    for j in range(y0, y1+1):
        print(board[i][j], end='')
    print()
