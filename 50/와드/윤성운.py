import sys
input = sys.stdin.readline

def dfs(r, c):
    stack = [(r, c)]
    while stack:
        current = stack.pop()
        if visited[current[0]][current[1]]:
            continue
        answer[current[0]][current[1]] = "."
        visited[current[0]][current[1]] = 1
        for d in range(4):
            nr = current[0] + dr[d]
            nc = current[1] + dc[d]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and arr[nr][nc] == arr[r][c]:
                stack.append((nr, nc))

    
R, C = map(int, input().split())
arr = [input() for _ in range(R)]
current = list(map(lambda x: int(x) - 1, input().split()))
history = input().strip()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
move_dict = {"U": [-1, 0], "D": [1, 0], "R": [0, 1], "L": [0, -1]}

answer = [["#"] * C for _ in range(R)]
visited = [[0] * C for _ in range(R)]

# 둘아다니면서 와드 박기
for behavior in history:
    if behavior == "W":
        if visited[current[0]][current[1]]:
            continue
        dfs(current[0], current[1])
    else:
        current[0] += move_dict[behavior][0]
        current[1] += move_dict[behavior][1]

# 마지막에 위치한 곳 밝히기
answer[current[0]][current[1]] = "."
for i in range(4):
    if 0 <= current[0] + dr[i] < R and 0 <= current[1] + dc[i] < C:
        answer[current[0] + dr[i]][current[1] + dc[i]] = "."

for i in range(R):
    print("".join(answer[i]))