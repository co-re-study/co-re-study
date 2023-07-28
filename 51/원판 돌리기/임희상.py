from collections import deque

N, M, T = map(int, input().split())

board = []
for _ in range(N):
    board.append(deque(map(int, input().split())))

commands = []
for _ in range(T):
    commands.append(list(map(int, input().split())))


def rotate(target, d, k):
    
    for _ in range(k):
        
        if d:
            target.append(target.popleft())
        else:
            target.appendleft(target.pop())
    
    return target


def erase():

    visited = set()
    targets = []
    flag = False
    for i in range(N):
        for j in range(M):
            if (i, j)not in visited and board[i][j]:
                stack = [(i, j)]
                target_set = {(i, j)}
                while stack:
                    r, c = stack.pop()
                    if (r, c) in visited:
                        continue
                    visited.add((r, c))
                    for nr, nc in [[r, c+1], [r, c-1], [r+1, c], [r-1, c]]:
                        if nc == M:
                            nc = 0
                        if nc == -1:
                            nc = M-1
                        if 0 <= nr < N and (nr, nc) not in visited:
                            if board[nr][nc] == board[i][j]:
                                target_set.add((nr, nc))
                                stack.append((nr, nc))
                                flag = True
                targets.append(target_set)
    for target_set in targets:
        if len(target_set) > 1:
            for target in target_set:
                board[target[0]][target[1]] = 0
    
    return flag


def flatten():

    avg = 0
    cnt = 0

    for i in range(N):
        for j in range(M):
            if board[i][j]:
                cnt += 1
                avg += board[i][j]
    if not cnt:
        return
    avg /= cnt

    for i in range(N):
        for j in range(M):
            if board[i][j]:
                if board[i][j] > avg:
                    board[i][j] -= 1
                elif board[i][j] < avg:
                    board[i][j] += 1



for command in commands:
    x, d, k = command
    s = x-1
    while s < N:
        board[s] = rotate(board[s], d, k)
        s += x
    if not erase():  # 성공여부를 return받음
        flatten()

answer = 0
for i in range(N):
    for j in range(M):
        answer += board[i][j]

print(answer)

