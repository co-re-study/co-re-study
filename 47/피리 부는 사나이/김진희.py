# 피리 부는 사나이
destination = {'D': (1, 0), 'R': (0, 1), 'U': (-1, 0), 'L': (0, -1)}
before = {(1, 0): 'U', (0, 1): 'L', (-1, 0): 'D', (0, -1): 'R'}


def dfs(x, y):
    global answer
    answer += 1
    stack = [(x, y)]
    while stack:
        cr, cc = stack.pop()
        arr[cr][cc] = answer
        for next in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = cr + next[0]
            nc = cc + next[1]
            # 내가 갈 방향이면 스택에 추가
            if next == destination[arrow[cr][cc]] and not arr[nr][nc]:
                stack.append((nr, nc))
            # 나에게 오는 방향이어도 스택에 추가
            elif 0 <= nr < n and 0 <= nc < m and arrow[nr][nc] == before[next] and not arr[nr][nc]:
                stack.append((nr, nc))


n, m = map(int, input().split())
arrow = [list(input()) for _ in range(n)]
arr = [[0] * m for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        if not arr[i][j]:
            dfs(i, j)
            
print(answer)
