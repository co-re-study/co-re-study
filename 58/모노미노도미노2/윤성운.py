import sys
input = sys.stdin.readline

N = int(input())
blue_arr = [[0] * 6 for _ in range(4)]
green_arr = [[0] * 4 for _ in range(6)]

dr = [0, 0, 0, 1]
dc = [0, 0, 1, 0]
acc = 0

for _ in range(N):
    t, r, c = map(int, input().split())
    nr1 = r
    nc1 = 0
    nr2 = r + dr[t]
    nc2 = dc[t]
    while nc1 != 5 and not blue_arr[nr1][nc1 + 1] and nc2 != 5 and not blue_arr[nr2][nc2 + 1]:
        nc1 += 1
        nc2 += 1
    blue_arr[nr1][nc1] = 1
    blue_arr[nr2][nc2] = 1
    while True:
        for i in range(6):
            for j in range(4):
                if not blue_arr[j][i]:
                    break
            else:
                acc += 1
                for j in range(4):
                    blue_arr[j][i] = 0
                for k in range(i - 1, -1, -1):
                    for j in range(4):
                        blue_arr[j][k + 1] = blue_arr[j][k]
                for j in range(4):
                    blue_arr[j][0] = 0
                break
        else:
            break
    while sum(list(zip(*blue_arr))[1]):
        for i in range(4):
            for j in range(4, -1, -1):
                blue_arr[i][j + 1] = blue_arr[i][j]
            blue_arr[i][0] = 0

    nr1 = 0
    nc1 = c
    nr2 = dr[t]
    nc2 = c + dc[t]
    while nr1 != 5 and not green_arr[nr1 + 1][nc1] and nr2 != 5 and not green_arr[nr2 + 1][nc2]:
        nr1 += 1
        nr2 += 1
    green_arr[nr1][nc1] = 1
    green_arr[nr2][nc2] = 1
    while True:
        for i in range(6):
            for j in range(4):
                if not green_arr[i][j]:
                    break
            else:
                acc += 1
                for j in range(4):
                    green_arr[i][j] = 0
                for k in range(i - 1, -1, -1):
                    for j in range(4):
                        green_arr[k + 1][j] = green_arr[k][j]
                for j in range(4):
                    green_arr[0][j] = 0
                break
        else:
            break
    while sum(green_arr[1]):
        for i in range(4, -1, -1):
            for j in range(4):
                green_arr[i + 1][j] = green_arr[i][j]
        for i in range(4):
            green_arr[0][i] = 0

print(acc)
print(sum(map(sum, blue_arr)) + sum(map(sum, green_arr)))
