from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(R)]
villains = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(3)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[[-1] * 3 for _ in range(C)] for _ in range(R)]

# 각 악당 별로 BFS 후 모든 좌표에 각 거리 기록
for v in range(3):
    villain = villains[v]
    queue = deque([(villain[0], villain[1], 0)])
    visited[villain[0]][villain[1]][v] = 0
    while queue:
        r, c, dist = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not arr[nr][nc] and visited[nr][nc][v] == -1:
                queue.append((nr, nc, dist + 1))
                visited[nr][nc][v] = dist + 1

# 모두 밟을 수 있는 좌표 중 가장 짧은 거리 찾기
min_distance = 10001
answer_cnt = 0
for r in range(R):
    for c in range(C):
        if min(visited[r][c]) >= 0:
            max_distance = max(visited[r][c])
            if max_distance < min_distance:
                min_distance = max_distance
                answer_cnt = 1
            elif max_distance == min_distance:
                answer_cnt += 1

if answer_cnt:
    print(min_distance)
    print(answer_cnt)
else:
    print(-1)