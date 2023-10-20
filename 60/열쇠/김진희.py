from collections import deque
import sys
input = sys.stdin.readline


def solve():
    global answer
    # 문은 넣고 갈 수 있는 곳 다 가면서 열쇠 모으고
    # 문을 다시 돌고
    while q:
        while q:
            cr, cc = q.pop()
            for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and arr[nr][nc] != '*':
                    find(nr, nc)
        for door in range(len(doors)):
            cr, cc = doors.popleft()
            if arr[cr][cc].lower() in keys:
                q.append((cr, cc))
            else:
                doors.append((cr, cc))


def find(x, y):
    global answer
    visited[x][y] = 1
    if arr[x][y] == '.':
        q.append((x, y))
    elif arr[x][y].islower():
        q.append((x, y))
        keys.add(arr[x][y])
    elif arr[x][y].isupper():
        if arr[x][y].lower() in keys:
            q.append((x, y))
        else:
            doors.append((x, y))
    elif arr[x][y] == '$':
        q.append((x, y))
        answer += 1


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]  # '.'빈칸 '*'벽 '$'문서 '대'문 '소'열쇠
    keys = set(input())

    answer = 0
    doors = deque()
    q = deque()
    visited = [[0] * M for _ in range(N)]

    # 가능한 시작점 찾기
    for j in range(M):
        if arr[0][j] != '*':
            find(0, j)
        if arr[-1][j] != '*':
            find(N - 1, j)

    for i in range(1, N - 1):
        if arr[i][0] != '*':
            find(i, 0)
        if arr[i][-1] != '*':
            find(i, M-1)

    solve()
    print(answer)
