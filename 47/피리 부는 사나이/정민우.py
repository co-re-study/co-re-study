# 완전히 분리된 경로의 그룹이 몇 그룹인지 알아내면 될듯.

direction = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
}

def search(i, j, d):
    global visited, ans

    now_visited = set()
    now_visited.add((i, j))
    while True:
        i, j = i + direction[d][0], j + direction[d][1]
        d = matrix[i][j]
        if (i, j) in visited:
            visited |= now_visited
            break
        elif (i, j) in now_visited:
            visited |= now_visited
            ans += 1
            break
        else:
            now_visited.add((i, j))

ans = 0
N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
visited = set()

for n in range(N):
    for m in range(M):
        if (n, m) not in visited:
            search(n, m, matrix[n][m])

print(ans)