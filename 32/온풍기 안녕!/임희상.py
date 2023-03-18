R, C, K = map(int, input().split())
board = [[0]*C for _ in range(R)]
coordinates = set()
check_set = set()
heaters = []
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]
for i in range(R):
    line = list(map(int, input().split()))
    for j in range(C):
        coordinates.add((i, j))
        if line[j]:
            if line[j] == 5:
                check_set.add((i, j))
            else:
                heaters.append((i, j, line[j]))
W = int(input())
walls = set()
for _ in range(W):
    r, c, t = map(int, input().split())
    if not t:
        walls.add((r-2, c-1, r-1, c-1))
    else:
        walls.add((r-1, c-1, r-1, c))


def find_destinations(x, y, d):
    destinations = []
    if (x+dr[d], y+dc[d]) in coordinates:
        if (min(x, x+dr[d]), min(y, y+dc[d]), max(x, x+dr[d]), max(y, y+dc[d])) not in walls:
            destinations.append((x+dr[d], y+dc[d]))
    if d < 3:
        sides = [(x+1, y), (x-1, y)]
    else:
        sides = [(x, y+1), (x, y-1)]
    for side in sides:
        if (side[0] + dr[d], side[1] + dc[d]) in coordinates:
            if (min(x, side[0]), min(y, side[1]), max(x, side[0]), max(y, side[1])) not in walls and \
                    (min(side[0], side[0] + dr[d]), min(side[1], side[1] + dc[d]), max(side[0], side[0] + dr[d]),
                     max(side[1], side[1] + dc[d])) not in walls:
                destinations.append((side[0] + dr[d], side[1] + dc[d]))
    return destinations


def heater_on(heater):
    power = 5
    targets = set()
    r, c, d = heater
    targets.add((r+dr[d], c+dc[d]))
    while power:
        new_targets = set()
        for target in targets:
            nr, nc = target
            board[nr][nc] += power
            for destination in find_destinations(nr, nc, d):
                new_targets.add(destination)
        targets = new_targets
        power -= 1


answer = 0
while answer < 101:
    answer += 1

    for heater in heaters:
        heater_on(heater)
    change_board = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            for d in range(1, 5):
                if (r+dr[d], c+dc[d]) in coordinates and board[r][c] > board[r+dr[d]][c+dc[d]] and \
                        (min(r, r+dr[d]), min(c, c+dc[d]), max(r, r+dr[d]), max(c, c+dc[d])) not in walls:
                    spread = (board[r][c] - board[r+dr[d]][c+dc[d]])//4
                    change_board[r+dr[d]][c+dc[d]] += spread
                    change_board[r][c] -= spread
    stack = []
    for r in range(R):
        for c in range(C):
            board[r][c] += change_board[r][c]
    visited = set()
    for r in range(R):
        if (r, 0) not in visited and board[r][0]:
            board[r][0] -= 1
            visited.add((r, 0))
        if (r, C-1) not in visited and board[r][C-1]:
            board[r][C-1] -= 1
            visited.add((r, C-1))
    for c in range(C):
        if (0, c) not in visited and board[0][c]:
            board[0][c] -= 1
            visited.add((0, c))
        if (R-1, c) not in visited and board[R-1][c]:
            board[R-1][c] -= 1
            visited.add((R-1, c))


    for coordinate in check_set:
        if board[coordinate[0]][coordinate[1]] < K:
            break
    else:
        break

print(answer)

