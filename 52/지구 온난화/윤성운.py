import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [input() for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

alive_positions = set()

for r in range(R):
    for c in range(C):
        if arr[r][c] == ".":
            continue
        cnt = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == "X":
                continue
            cnt += 1
        if cnt < 3:
            alive_positions.add((r, c))

min_r, max_r, min_c, max_c = 11, -1, 11, -1
for position in alive_positions:
    min_r = min(min_r, position[0])
    max_r = max(max_r, position[0])
    min_c = min(min_c, position[1])
    max_c = max(max_c, position[1])

for r in range(min_r, max_r + 1):
    row = ""
    for c in range(min_c, max_c + 1):
        row += arr[r][c] if (r, c) in alive_positions else "."
    print(row)