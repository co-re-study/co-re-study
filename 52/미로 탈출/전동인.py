from collections import deque

r, c = map(int, input().strip().split())
si, sj = map(int, input().strip().split())
ei, ej = map(int, input().strip().split())
maze = [list(map(int, input().strip().split())) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    visited = [[[0] * 2 for _ in range(c)] for _ in range(r)]
    queue = deque([(si-1, sj-1, 0, 0)])  # x, y, distance, wall_break
    visited[si-1][sj-1][0] = 1

    while queue:
        x, y, dist, wall_break = queue.popleft()
        if (x, y) == (ei-1, ej-1):
            return dist

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < r and 0 <= ny < c:
                # 다음 칸이 벽이고 깰 수 있다면
                if maze[nx][ny] == 1 and wall_break == 0:
                    if not visited[nx][ny][1]:
                        visited[nx][ny][1] = 1
                        queue.append((nx, ny, dist+1, 1))
                # 다음 칸으로 이동할 수 있다면
                elif maze[nx][ny] == 0:
                    if not visited[nx][ny][wall_break]:
                        visited[nx][ny][wall_break] = 1
                        queue.append((nx, ny, dist+1, wall_break))
    return -1


print(bfs())
