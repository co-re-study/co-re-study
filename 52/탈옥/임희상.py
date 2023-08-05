from collections import deque

T = int(input())

def bfs(start):

    view = [[h*w]*(w+2) for _ in range(h+2)]
    queue = deque([[start[0], start[1], 0]])

    while queue:
        r, c, cost = queue.popleft()
        
        if view[r][c] != h*w:
            continue
        view[r][c] = cost
        
        for nr, nc in [[r, c+1], [r,c-1], [r+1,c], [r-1,c]]:
            if 0 <= nr < h+2 and 0 <= nc < w+2 and view[nr][nc] > cost:
                if board[nr][nc] == '.' or board[nr][nc] == '$':
                    queue.appendleft((nr, nc, cost))
                elif board[nr][nc] == '#':
                    queue.append((nr, nc, cost+1))
    
    return view


for _ in range(T):

    h, w = map(int, input().split())
    
    board = [['.']*(w+2)]
    for _ in range(h):
        board.append(['.'] + list(input()) + ['.'])
    board.append(['.']*(w+2))
    
    targets = []
    for i in range(h+2):
        for j in range(w+2):
            if board[i][j] == '$':
                targets.append((i, j))

    view_1 = bfs([0, 0])
    view_2 = bfs([targets[0][0], targets[0][1]])
    view_3 = bfs([targets[1][0], targets[1][1]])

    answer = h*w
    for i in range(h+2):
        for j in range(w+2):
            cost_sum = view_1[i][j] + view_2[i][j] + view_3[i][j]
            if board[i][j] == '#':
                answer = min(cost_sum-2, answer)
            if board[i][j] == '.':
                answer = min(cost_sum, answer)
    
    print(answer)