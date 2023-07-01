from collections import defaultdict


def route(stack):
    global cnt, visited

    si, sj = stack[0]
    while stack:
        i, j = stack.pop()
        if visited[(i, j)]:
            if visited[(i, j)] == (si, sj):
                cnt += 1
            break
        visited[(i, j)] = (si, sj)
        di, dj = field[i][j]
        stack.append((i+di, j+dj))


direction = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
n, m = map(int, input().split())
field = [[direction[s] for s in list(input())] for _ in range(n)]

cnt = 0
visited = defaultdict(tuple)
for i in range(n):
    for j in range(m):
        stack = [(i, j)]
        route(stack)
print(cnt)
