import sys
input = sys.stdin.readline

testcase = int(input())
for _ in range(testcase):
    h, w = map(int, input().split())
    arr = ["." + input().rstrip() + "." for _ in range(h)]
    arr.insert(0, "." * (w + 2))
    arr.append("." * (w + 2))

    stack = [(0, 0)]
    visited = [[-1] * (w + 2) for _ in range(h + 2)]
    keys = set(input().rstrip())
    answer_position = set()

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    answer = 0
    while stack:
        r, c = stack.pop()
        if visited[r][c] >= len(keys):
            continue
        visited[r][c] = len(keys)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < h + 2 and 0 <= nc < w + 2 and visited[nr][nc] < len(keys):
                if arr[nr][nc] == ".":
                    stack.append((nr, nc))
                elif arr[nr][nc] == "*":
                    continue
                elif arr[nr][nc] == "$":
                    answer_position.add((nr, nc))
                    stack.append((nr, nc))
                elif 97 <= ord(arr[nr][nc]) <= 122:
                    if arr[nr][nc] in keys:
                        stack.append((nr, nc))
                    else:
                        keys.add(arr[nr][nc])
                        stack = [(nr, nc)]
                elif chr(ord(arr[nr][nc]) + 32) in keys:
                    stack.append((nr, nc))

    print(len(answer_position))
