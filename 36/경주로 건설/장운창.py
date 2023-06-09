from collections import deque
def solution(board):
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    noback = (2, 3, 0, 1)
    N = len(board)
    myq = deque()
    myq.append((0, 0, 0, 0, {(0, 0)}))
    myq.append((0, 0, 1, 0, {(0, 0)}))
    minval = float('inf')
    pathdict = dict()
    while myq:
        y, x, prevd, price, visited = myq.popleft()
        for d in range(4):
            ny = y+dy[d]
            nx = x+dx[d]
            if 0<=ny<N and 0<=nx<N and not board[ny][nx] and (ny, nx) not in visited:
                if prevd == d:
                    if ny==N-1 and nx == N-1:
                        if minval > price+100:
                            minval = price+100
                            break
                    else:
                        if (ny, nx) in pathdict and pathdict[(ny, nx)] < price+100:
                            continue
                        pathdict[(ny, nx)] = price+100
                        myq.append((ny, nx, d, price+100, visited|{(ny, nx)}))
                else:
                    if ny==N-1 and nx == N-1:
                        if minval > price+600:
                            minval = price+600
                            break
                    else:
                        if (ny, nx) in pathdict and pathdict[(ny, nx)] < price+400:
                            continue
                        pathdict[(ny, nx)] = price+600
                        myq.append((ny, nx, d, price+600, visited|{(ny, nx)}))
    return minval
