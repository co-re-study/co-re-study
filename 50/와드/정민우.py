from collections import deque

di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
i, j = map(lambda x: int(x) - 1, input().split())

ward = set()
for d in input():
    if d == 'W':
        ward.add((i, j))
    elif d == 'U':
        i -= 1
    elif d == 'D':
        i += 1
    elif d == 'R':
        j += 1
    elif d == 'L':
        j -= 1

for wi, wj in ward:
    if matrix[wi][wj] != '.':
        now = matrix[wi][wj]
        Q = deque([(wi, wj)])
        while Q:
            for _ in range(len(Q)):
                qi, qj = Q.popleft()
                if matrix[qi][qj] != '.':
                    matrix[qi][qj] = '.'
                    for d in range(4):
                        ni, nj = qi + di[d], qj + dj[d]
                        if 0 <= ni < R and 0 <= nj < C and matrix[ni][nj] == now:
                            Q.append((ni, nj))

matrix[i][j] = '.'
for d in range(4):
    ni, nj = i + di[d], j + dj[d]
    if 0 <= ni < R and 0 <= nj < C and matrix[ni][nj] != '.':
        matrix[ni][nj] = '.'

for r in range(R):
    for c in range(C):
        if matrix[r][c] != '.':
            matrix[r][c] = '#'
    print(''.join(matrix[r]))
