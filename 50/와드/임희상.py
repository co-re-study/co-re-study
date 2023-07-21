R, C = map(int, input().split())

board = []
visited = [[0]*C for _ in range(R)]
for _ in range(R):
    board.append(list(input()))

current = list(map(int, input().split()))
current = [current[0]-1, current[1]-1]

dir_dict = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}
dir_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(start, target):
    stack = [start]
    local_visited = set()
    while stack:
        r, c = stack.pop()
        if visited[r][c]:  # 이미 와드 시야가 있음
            return
        if (r, c) in local_visited:
            continue
        local_visited.add((r, c))
        for dr, dc in dir_list:
            if 0 <= r+dr < R and 0 <= c+dc < C and board[r+dr][c+dc] == target:
                stack.append((r+dr, c+dc))
    
    for r, c in local_visited:
        visited[r][c] = 1
            

for order in list(input()):

    if order == 'W':
        dfs(current, board[current[0]][current[1]])
    else:
        current = [current[0]+dir_dict[order][0], current[1]+dir_dict[order][1]]

visited[current[0]][current[1]] = 1
for dr, dc in dir_list:
        if 0 <= current[0]+dr < R and 0 <= current[1]+dc < C:
            visited[current[0]+dr][current[1]+dc] = 1


for r in range(R):
    line = []
    for c in range(C):
        if visited[r][c]:
            line.append('.')
        else:
            line.append('#')
    print(''.join(line))