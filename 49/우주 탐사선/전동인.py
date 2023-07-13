def check(start, time, depth):
    global min_time

    if depth == n:
        min_time = min(time, min_time)
        return

    for destination in range(n):
        if visited[destination] == 0:
            visited[destination] = 1
            check(destination, time + matrix[start][destination], depth+1)
            visited[destination] = 0


n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for h in range(n):
    for i in range(n):
        for j in range(n):
            matrix[i][j] = min(matrix[i][j], matrix[i][h] + matrix[h][j])

visited = [0 for _ in range(n)]
visited[k] = 1
min_time = 1000*n


check(k, 0, 1)

print(min_time)
