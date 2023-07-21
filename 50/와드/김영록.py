from collections import deque


def union(x, y):
    target = board[x][y]
    queue = deque([[x, y]])
    ans[x][y] = '.'
    while queue:
        x0, y0 = queue.popleft()
        for d in direction:
            x1 = x0+direction[d][0]
            y1 = y0+direction[d][1]
            if 0 <= x1 < r and 0 <= y1 < c and board[x1][y1] == target and ans[x1][y1] == '#':
                ans[x1][y1] = '.'
                queue.append([x1, y1])


direction = {
    'U': [-1, 0],
    'D': [1, 0],
    'L': [0, -1],
    'R': [0, 1],
}
r, c = map(int, input().split())
board = [input() for _ in range(r)]
ans = [['#']*c for _ in range(r)]
r0, c0 = map(int, input().split())
r0 -= 1
c0 -= 1
history = input()
for h in history:
    if h == 'W':
        union(r0, c0)
    else:
        r0 += direction[h][0]
        c0 += direction[h][1]
ans[r0][c0] = '.'
for d in direction:
    if 0 <= r0+direction[d][0] < r and 0 <= c0+direction[d][1] < c:
        ans[r0+direction[d][0]][c0+direction[d][1]] = '.'
for a in ans:
    print(''.join(a))
