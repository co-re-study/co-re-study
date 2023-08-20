import sys
input = sys.stdin.readline
while True:
    N = int(input())
    if not N:
        break
    rooms = [[]]
    for _ in range(N):
        info = input().split()
        rooms.append([info[0], int(info[1]), list(map(int, info[2:-1]))])
    queue = [[1, 0]]
    ans = 'No'
    visited = [-1]*(N+1)
    while queue:
        curr, acc = queue.pop()
        types, cost, targets = rooms[curr]
        if visited[curr] >= acc:
            continue
        visited[curr] = acc
        if types == 'L':
            acc = max(cost, acc)
        elif types == 'T':
            acc -= cost
        if acc < 0:
            continue
        if curr == N:
            ans = 'Yes'
            break
        for target in targets:
            queue.append([target, acc])
    print(ans)
