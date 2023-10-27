n, m, h, p = map(int, input().split())

arr = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, d = map(int, input().split())
    arr[x - 1][y - 1].append(d)

trees = set()
for _ in range(h):
    x, y = map(int, input().split())
    trees.add((x - 1, y - 1))

# 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

r = n // 2
c = n // 2
d = 0
character_move = [(r, c, d)]

# 술래 이동 및 방향 정보 채우기
for i in range(1, n):
    for j in range(2):
        for k in range(i):
            r += dr[d]
            c += dc[d]
            if k < i - 1:
                character_move.append((r, c, d))
        d = (d + 1) % 4
        character_move.append((r, c, d))
for i in range(n - 1):
    r += dr[d]
    c += dc[d]
    character_move.append((r, c, d))
d = 2
character_move[-1] = (0, 0, 2)
for i in range(n - 1):
    r += dr[d]
    c += dc[d]
    character_move.append((r, c, d))
d = 1
character_move[-1] = (r, c, d)
for i in range(n - 1, 0, -1):
    for j in range(2):
        for k in range(i):
            r += dr[d]
            c += dc[d]
            if k < i - 1:
                character_move.append((r, c, d))
        d = (d - 1) if d > 0 else 3
        character_move.append((r, c, d))
character_move.pop()

character_idx = 0
answer = 0

for turn in range(1, p + 1):
    # 도망자 이동
    new_locations = []
    stack = [(character_move[character_idx][0], character_move[character_idx][1], 0)]
    visited = set()
    while stack:
        current = stack.pop()
        while arr[current[0]][current[1]]:
            d = arr[current[0]][current[1]].pop()
            nr = current[0] + dr[d]
            nc = current[1] + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                if nr != character_move[character_idx][0] or nc != character_move[character_idx][1]:
                    new_locations.append((nr, nc, d))
                else:
                    new_locations.append((current[0], current[1], d))
            else:
                nd = (d + 2) % 4
                nr = current[0] + dr[nd]
                nc = current[1] + dc[nd]
                if nr != character_move[character_idx][0] or nc != character_move[character_idx][1]:
                    new_locations.append((nr, nc, nd))
                else:
                    new_locations.append((current[0], current[1], d))
        if current[2] == 3:
            continue
        for i in range(4):
            nr = current[0] + dr[i]
            nc = current[1] + dc[i]
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                stack.append((nr, nc, current[2] + 1))
                visited.add((nr, nc))
    for location in new_locations:
        arr[location[0]][location[1]].append(location[2])

    # 술래 이동 및 도망자 잡기
    character_idx = (character_idx + 1) % ((n ** 2 * 2) - 2)
    for i in range(3):
        nr = character_move[character_idx][0] + dr[character_move[character_idx][2]] * i
        nc = character_move[character_idx][1] + dc[character_move[character_idx][2]] * i
        if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in trees:
            if arr[nr][nc]:
                answer += len(arr[nr][nc]) * turn
                arr[nr][nc].clear()

print(answer)
