# def ward(current_alphabet, y, x, visit):
#     board[y][x] = '.'
#     visit.add((y, x))
#     for i in range(4):
#         if 0 <= y+dy[i] < R and 0 <= x+dx[i] < C and (y+dy[i], x+dx[i]) not in visit:
#             r = y + dy[i]
#             c = x + dx[i]
#             if mat[r][c] == current_alphabet:
#                 ward(current_alphabet, r, c, visit)

from collections import deque
import sys

def ward(current_alphabet, y, x):
    stack = deque([(y, x)])
    board[y][x] = '.'
    while stack:
        a, b = stack.popleft()
        # board[a][b] = '.'

        for i in range(4):
            r = a + dy[i]
            c = b + dx[i]
            if 0 <= r < R and 0 <= c < C and (r, c) and board[r][c] == '#' and mat[r][c] == current_alphabet :
                stack.append((r, c))
                board[r][c] = '.'


R, C = map(int, sys.stdin.readline().split())

mat = [list(sys.stdin.readline()) for _ in range(R)]

y, x = map(int, sys.stdin.readline().split())
arr = sys.stdin.readline()

board = [['#'] * C for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

y, x = y - 1, x - 1

for i in arr:

    if i == 'W':
        ward(mat[y][x], y, x)
    elif i == 'U':
        y += dy[0]
        x += dx[0]
    elif i == 'D':
        y += dy[1]
        x += dx[1]
    elif i == 'L':
        y += dy[2]
        x += dx[2]
    elif i == 'R':
        y += dy[3]
        x += dx[3]


for j in range(4):
    if 0 <= y+dy[j] < R and 0 <= x+dx[j] < C:
        board[y+dy[j]][x+dx[j]] = '.'
board[y][x] = '.'

for i in board:
    print("".join(i))