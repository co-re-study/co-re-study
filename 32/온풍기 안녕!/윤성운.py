from copy import deepcopy

def blow():
    for heater in heaters:
        direction = heaters[heater]
        next_positions = {(heater[0] + dr[direction], heater[1] + dc[direction], 1)}

        for power in range(5, 0, -1):
            current_positions = set(next_positions)
            next_positions = set()
            for position in current_positions:
                if position[0] < 0 or position[0] >= R or position[1] < 0 or position[1] >= C:
                    continue
                arr[position[0]][position[1]] += power
                if (position[0], position[1]) not in walls or direction not in walls[(position[0], position[1])]:
                    next_positions.add((position[0] + dr[direction], position[1] + dc[direction], position[2] + 1))
                if (position[0], position[1]) not in walls or block[direction][0] not in walls[(position[0], position[1])]:
                    if (position[0] + dn[direction][0][0], position[1] + dn[direction][0][1]) not in walls or direction not in walls[(position[0] + dn[direction][0][0], position[1] + dn[direction][0][1])]:
                        next_positions.add((position[0] + dr[direction] + dn[direction][0][0], position[1] + dc[direction] + dn[direction][0][1], position[2] + 1))
                if (position[0], position[1]) not in walls or block[direction][1] not in walls[(position[0], position[1])]:
                    if (position[0] + dn[direction][1][0], position[1] + dn[direction][1][1]) not in walls or direction not in walls[(position[0] + dn[direction][1][0], position[1] + dn[direction][1][1])]:
                        next_positions.add((position[0] + dr[direction] + dn[direction][1][0], position[1] + dc[direction] + dn[direction][1][1], position[2] + 1))

def adjustTemp():
    new_arr = deepcopy(arr)
    for r in range(R):
        for c in range(C):
            for d in range(1, 5):
                if (r, c) in walls and d in walls[(r, c)]:
                    continue
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < R and 0 <= nc < C:
                    if arr[r][c] > arr[nr][nc]:
                        new_arr[r][c] -= (arr[r][c] - arr[nr][nc]) // 4
                        new_arr[nr][nc] += (arr[r][c] - arr[nr][nc]) // 4
    return new_arr


def reduceTemp():
    for r in [0, R-1]:
        for c in [0, C-1]:
            if arr[r][c]:
                arr[r][c] -= 1

    for r in range(1, R-1):
        for c in [0, C-1]:
            if arr[r][c]:
                arr[r][c] -= 1

    for r in [0, R-1]:
        for c in range(1, C-1):
            if arr[r][c]:
                arr[r][c] -= 1


R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
walls = dict()
for _ in range(W):
    x, y, d = map(int, input().split())
    if d:
        if (x-1, y-1) in walls:
            walls[(x-1, y-1)].append(1)
        else:
            walls[(x-1, y-1)] = [1]
        if (x-1, y) in walls:
            walls[(x-1, y)].append(2)
        else:
            walls[(x - 1, y)] = [2]

    else:
        if (x-1, y-1) in walls:
            walls[(x-1, y-1)].append(3)
        else:
            walls[(x-1, y-1)] = [3]
        if (x-2, y-1) in walls:
            walls[(x-2, y-1)].append(4)
        else:
            walls[(x-2, y-1)] = [4]

heaters = dict()
check_positions = []

for r in range(R):
    for c in range(C):
        if arr[r][c]:
            if arr[r][c] == 5:
                check_positions.append((r, c))
            else:
                heaters[(r, c)] = arr[r][c]

arr = [[0] * C for _ in range(R)]

dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]
dn = [(), [(-1, 0), (1, 0)], [(-1, 0), (1, 0)], [(0, 1), (0, -1)], [(0, 1), (0, -1)]]
block = [(), (3, 4), (3, 4), (1, 2), (1, 2)]

for chocolate in range(1, 101):
    blow()
    arr = adjustTemp()
    reduceTemp()
    for position in check_positions:
        if arr[position[0]][position[1]] < K:
            break
    else:
        break
else:
    chocolate = 101

print(chocolate)