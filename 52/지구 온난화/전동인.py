from copy import deepcopy

r, c = map(int, input().split())
field = [list(input()) for _ in range(r)]


def check(i, j):
    ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cnt = 0
    for d in ds:
        di, dj = d
        if 0 <= i + di < r and 0 <= j + dj < c:
            if field[i + di][j + dj] == '.':
                cnt += 1
        else:
            cnt += 1
    if cnt >= 3:
        return '.'
    else:
        return 'X'


new_field = deepcopy(field)
for i in range(r):
    for j in range(c):
        if field[i][j] == 'X':
            new_field[i][j] = check(i, j)
field = new_field

while 'X' not in field[0]:
    field.pop(0)
while 'X' not in field[-1]:
    field.pop()


field = list(map(list, zip(*field)))

while 'X' not in field[0]:
    field.pop(0)
while 'X' not in field[-1]:
    field.pop()


field = list(map(list, zip(*field)))

for el in field:
    print(''.join(el))
