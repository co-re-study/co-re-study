board = []
for i in range(10):
    line = list(input().strip())
    for j in range(10):
        if line[j] == 'O':
            line[j] = True
        else:
            line[j] = False
    board.append(line)

dx = [-1, 1, 0, 0, 0]
dy = [0, 0, 0, -1, 1]

def switch(x, y, board):
    for k in range(5):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < 10 and 0 <= ny < 10:
            board[ny][nx] = not board[ny][nx]

answer = float('inf')

for state in range(1 << 10):
    temp_board = [line[:] for line in board]
    counts = 0

    for i in range(10):
        if state & (1 << i):
            switch(i, 0, temp_board)
            counts += 1

    for y in range(1, 10):
        for x in range(10):
            if temp_board[y - 1][x]:
                switch(x, y, temp_board)
                counts += 1

    if all(not val for val in temp_board[9]):
        answer = min(answer, counts)

print(answer if answer != float('inf') else -1)
