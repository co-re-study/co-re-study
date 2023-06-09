# 사각형을 네 구역으로 나눠 보면서 분할정복 재귀

def comp(size, y, x):
    global comp_video

    comp_video += "("
    for i in [y, y + size // 2]:
        for j in [x, x + size // 2]:
            now = check_color(size // 2, i, j)
            if now:
                comp_video += now
            else:
                comp(size // 2, i, j)
    comp_video += ")"


def check_color(size, y, x):
    diff_color = 0 if video[y][x] == 1 else 1
    is_same = True
    for i in range(y, y + size):
        if diff_color in video[i][x:x + size]:
            is_same = False
            break
    if is_same:
        return "0" if diff_color == 1 else "1"
    else:
        return False


N = int(input())
video = [list(map(int, list(input()))) for _ in range(N)]
comp_video = ""
if check_color(N, 0, 0):
    print(check_color(N, 0, 0))
else:
    comp(N, 0, 0)
    print(comp_video)

