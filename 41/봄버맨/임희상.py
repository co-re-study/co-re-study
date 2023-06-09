R, C, N = map(int, input().split())
board = []

for i in range(R):
    line = input()
    board_line = []
    for j in range(C):
        if line[j] == 'O':
            board_line.append(2)
        else:
            board_line.append(0)
    board.append(board_line)

# 처음 1초는 아무것도 안하니 시간을 1로
current = 1
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
while current <= N:
    if current == N:
        break

    for r in range(R):
        for c in range(C):
            if not board[r][c]:
                board[r][c] = 3
            else:
                board[r][c] -= 1

    current += 1
    if current == N:
        break

    explode = set()
    for r in range(R):
        for c in range(C):
            if board[r][c]:
                board[r][c] -= 1
                if not board[r][c]:
                    explode.add((r, c))
                    for d in range(4):
                        if 0 <= r+dr[d] < R and 0 <= c+dc[d] < C:
                            explode.add((r+dr[d], c+dc[d]))
    for coord in explode:
        r, c = coord
        board[r][c] = 0
    current += 1

for i in range(R):
    line = []
    for j in range(C):
        if board[i][j]:
            line.append('O')
        else:
            line.append('.')
    print(''.join(line))

