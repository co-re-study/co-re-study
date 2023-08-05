R, C = map(int, input().split())

board = []
for _ in range(R):
    board.append(list(input()))

targets = set()

for i in range(R):
    for j in range(C):
        if board[i][j] == 'X':
            cnt = 0
            for nr, nc in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if not (0<=nr<R and 0<=nc<C) or board[nr][nc] == '.':
                    cnt += 1
            if cnt > 2:
                targets.add((i, j))

r_start, c_start, r_end, c_end = R-1, C-1, 0, 0
for i in range(R):
    for j in range(C):
        if (i, j) in targets:
            board[i][j] = '.'
        if board[i][j] == 'X':
            r_start, c_start, r_end, c_end = min(r_start, i), min(c_start, j), max(r_end, i), max(c_end, j)

for i in range(r_start, r_end+1):
    print(''.join(board[i][c_start:c_end+1]))



