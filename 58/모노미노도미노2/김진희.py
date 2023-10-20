def block_go_down(blocks):
    size = len(blocks)
    while True:
        new_blocks = []
        for cr, cc in blocks:
            nr, nc = cr + 1, cc
            if nr < 10 and arr[nr][nc] == 0:
                new_blocks.append((nr, nc))
        if len(new_blocks) == size:
            blocks = new_blocks
        else:
            break
    for x, y in blocks:
        arr[x][y] = T


def block_go_right(blocks):
    size = len(blocks)
    while True:
        new_blocks = []
        for cr, cc in blocks:
            nr, nc = cr, cc + 1
            if nc < 10 and arr[nr][nc] == 0:
                new_blocks.append((nr, nc))
        if len(new_blocks) == size:
            blocks = new_blocks
        else:
            break
    for x, y in blocks:
        arr[x][y] = T


def 가로한줄():
    global answer
    flag = False
    for i in range(6, 10):
        if arr[i][0] and arr[i][1] and arr[i][2] and arr[i][3]:
            answer += 1
            flag = True
            for k in range(i, 3, -1):
                arr[k][0], arr[k][1], arr[k][2], arr[k][3] = arr[k - 1][0], arr[k - 1][1], arr[k - 1][2], arr[k - 1][3]
    return flag


def 세로한줄():
    global answer
    flag = False
    for j in range(6, 10):
        if arr[0][j] and arr[1][j] and arr[2][j] and arr[3][j]:
            answer += 1
            flag = True
            for k in range(j, 3, -1):  # 거꾸로 올라가야지
                arr[0][k], arr[1][k], arr[2][k], arr[3][k] = arr[0][k - 1], arr[1][k - 1], arr[2][k - 1], arr[3][k - 1]
    return flag


def 가로땡기기(x):
    for k in range(9, 3, -1):  # 4번 줄까지 바꿔줘야함
        arr[k][0], arr[k][1], arr[k][2], arr[k][3] = arr[k - x][0], arr[k - x][1], arr[k - x][2], arr[k - x][3]


def 세로땡기기(x):
    for k in range(9, 3, -1):
        arr[0][k], arr[1][k], arr[2][k], arr[3][k] = arr[0][k - x], arr[1][k - x], arr[2][k - x], arr[3][k - x]


N = int(input())
arr = [[0] * 10 for _ in range(10)]

answer = 0
for tc in range(N):
    T, X, Y = map(int, input().split())
    # [1] 블록 넣기
    if T == 1:
        block_go_down([(X, Y)])
        block_go_right([(X, Y)])
    elif T == 2:
        block_go_down([(X, Y + 1), (X, Y)])
        block_go_right([(X, Y + 1), (X, Y)])
    else:
        block_go_down([(X + 1, Y), (X, Y)])
        block_go_right([(X + 1, Y), (X, Y)])

    # [2] 가로 한 줄 채운거 없애고 없앤 만큼씩 내리기
    가로한줄()
    세로한줄()

    # [3] 4,5 줄에 있으면 끝에 지우고 땡기기
    cnt = 0
    if arr[4][0] or arr[4][1] or arr[4][2] or arr[4][3]:
        cnt += 1
    if arr[5][0] or arr[5][1] or arr[5][2] or arr[5][3]:
        cnt += 1
    if cnt:
        가로땡기기(cnt)
        cnt = 0
    if arr[0][4] or arr[1][4] or arr[2][4] or arr[3][4]:
        cnt += 1
    if arr[0][5] or arr[1][5] or arr[2][5] or arr[3][5]:
        cnt += 1
    if cnt:
        세로땡기기(cnt)

acc = 0
for i in range(6, 10):
    for j in range(4):
        acc += (arr[i][j] > 0)
        acc += (arr[j][i] > 0)
print(answer)
print(acc)