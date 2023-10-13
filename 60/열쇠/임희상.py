T = int(input())
answers = []
for _ in range(T):

    h, w = map(int, input().split())

    board = []
    stack = []
    targets = set()
    doors = {}
    collected_keys = set()
    for i in range(h):
        line = list(input())
        board.append(line)

        for j in range(w):
            if line[j] == '$':
                targets.add((i, j))
            if line[j].isalpha():
                if line[j].isupper():
                    try:
                        doors[line[j].lower()].add((i, j))
                    except:
                        doors[line[j].lower()] = {(i, j)}
            if line[j] != '*' and (i == 0 or i == h-1 or j == 0 or j == w-1):
                stack.append((i, j))
                if line[j].isalpha() and line[j].islower():
                    collected_keys.add(line[j])

    collected_keys = collected_keys.union(set(input()))
    answer = 0
    visited = set()

    while stack:

        r, c = stack.pop()

        if (r, c) in visited:
            continue
        visited.add((r, c))
        if (r, c) in targets:
            answer += 1
            targets.remove((r, c))
        
        if board[r][c].isalpha():
            if board[r][c].islower():
                collected_keys.add(board[r][c])
                if board[r][c] in doors.keys():
                    for coord in doors[board[r][c]]:
                        if coord in visited:
                            visited.discard(coord)
                            stack.append(coord)

            else:
                if board[r][c].lower() not in collected_keys:
                    continue

        for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < h and 0 <= nc < w and (nr, nc) not in visited:
                if board[nr][nc] != '*':
                    stack.append((nr, nc))

    answers.append(answer)

for answer in answers:
    print(answer)