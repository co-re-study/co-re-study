R, C, N = map(int,input().split())
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
maxboard = set()
queue = []
while True:
    bomb = set()
    for i in range(R):
        line = input()
        for j in range(C):
            maxboard.add((i, j))
            if line[j] == 'O':
                bomb.add((i, j))
    queue.append(bomb)
    timer = 0
    if N == timer:
        break
    # NOTHING
    timer = 1
    if N == timer:
        break
    while True:
        # BOMB READY
        timer += 1
        queue.append(set(maxboard - queue[-1]))
        if N == timer:
            break
        # BOMB!
        timer += 1
        target = queue.pop(0)
        for i, j in target:
            for d in range(4):
                if (i+dy[d], j+dx[d]) in queue[-1]:
                    queue[-1].discard((i+dy[d], j+dx[d]))
        if N == timer:
            break
    if N == timer:
        break
bombs = set()
if len(queue) == 2:
    bombs = set(queue[0]|queue[-1])
else:
    bombs = queue[-1]
for i in range(R):
    for j in range(C):
        if (i, j) in bombs:
            print('O', end='')
        else:
            print('.', end='')
    print()