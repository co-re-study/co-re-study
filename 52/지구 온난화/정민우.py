R, C = map(int, input().split())
matrix = [['.'] * (C + 2)] + [['.'] + list(input()) + ['.'] for _ in range(R)] + [['.'] * (C + 2)]
land = set()
for r in range(1, R + 1):
    for c in range(1, C + 1):
        if matrix[r][c] == 'X':
            count = 0
            for d in ((0, -1), (1, 0), (0, 1), (-1, 0)):
                if matrix[r + d[0]][c + d[1]] == '.':
                    count += 1
                    if count == 3:
                        break
            if count < 3:
                land.add((r, c))

top = min(land)[0]
bottom = max(land)[0] + 1
left = min(land, key=lambda x: x[1])[1]
right = max(land, key=lambda x: x[1])[1] + 1

for i in range(top, bottom):
    for j in range(left, right):
        if (i, j) in land:
            print('X', end='')
        else:
            print('.', end='')
    print()