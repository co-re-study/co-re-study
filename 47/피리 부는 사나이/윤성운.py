import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

if (N, M) == (1, 1):
    print(1)
    exit(0)

visited = [[0] * M for _ in range(N)]
answer = 0

direction_dict = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}

for r in range(N):
    for c in range(M):
        if visited[r][c]:
            continue
        nr, nc = r, c
        tmp_visited = set() # 현재 위치에서부터 방문 기록 저장
        while not visited[nr][nc]:
            visited[nr][nc] = 1
            tmp_visited.add((nr, nc))
            nr, nc = nr + direction_dict[arr[nr][nc]][0], nc + direction_dict[arr[nr][nc]][1]
        # 원래 밟았던 곳을 또 밟았다면 safe zone 추가 x
        if (nr, nc) not in tmp_visited:
            continue
        answer += 1

print(answer)