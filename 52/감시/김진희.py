def no_cctv(visited, depth):
    global answer

    if depth == len(cctv):
        if visited:
            answer = min(answer, room - len(visited))
        return

    i, j, camera = cctv[depth]
    for c in range(arrow[camera][0]):  # 몇 번 재귀로 들어갈건지
        visit = set()
        for d in arrow[camera][1]:  # 어느 방향 보는지
            nr, nc = i + di[(d + c) % 4], j + dj[(d + c) % 4]
            while 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 6:
                    break
                if (nr, nc) not in visited and not arr[nr][nc]:
                    visit.add((nr, nc))
                nr += di[(d + c) % 4]  # 더할 값, d+c 라는 것과 % 4 해야 하는 것
                nc += dj[(d + c) % 4]
        no_cctv(visited.union(visit), depth + 1)


di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]
arrow = {1: [4, [0]], 2: (2, [0, 2]), 3: (4, [0, 1]), 4: (4, [1, 2, 0]), 5: (1, [0, 1, 2, 3])}

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

cctv = []  # (r, c, 유형)
wall = 0
for start_r in range(n):
    for start_c in range(m):
        if arr[start_r][start_c] in arrow:
            cctv.append((start_r, start_c, arr[start_r][start_c]))
        elif arr[start_r][start_c] == 6:
            wall += 1
# cctv가 없으면
if not cctv:
    print(m * n - wall)
    exit(0)

room = m * n - wall - len(cctv)
answer = 987654321
no_cctv(set(), 0)  # set()에 감시되는 빈 방만 넣어서 room - len(set())을 답으로 하자

if answer < 987654321:
    print(answer)
else:  # 아예 방이 없으면 0
    print(0)
