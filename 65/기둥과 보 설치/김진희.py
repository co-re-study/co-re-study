def solution(n, build_frame):
    answer = []
    n += 1
    arr = [[[0, 0] for _ in range(n)] for _ in range(n)]  # [기둥, 보] 있으면 1
    for x, y, container, build in build_frame:
        if container:  # 보
            if build:
                if check1(arr, x, y, n):
                    arr[x][y][1] = 1
            else:
                arr[x][y][1] = 0
                if not remove1(arr, x, y, n):
                    arr[x][y][1] = 1

        else:  # 기둥
            if build:
                if check0(arr, x, y):
                    arr[x][y][0] = 1
            else:
                arr[x][y][0] = 0
                if not remove0(arr, x, y, n):
                    arr[x][y][0] = 1

    for i in range(n):
        for j in range(n):
            for k in range(2):
                if arr[i][j][k]:
                    answer.append([i, j, k])
    return answer


def check0(arr, x, y):
    if y == 0: return True
    if 0 <= y-1 and arr[x][y-1][0]: return True
    if 0 <= x-1 and arr[x-1][y][1]: return True
    if arr[x][y][1]: return True
    return False


def check1(arr, x, y, n):
    if 0 <= y - 1 and arr[x][y-1][0]: return True
    if x + 1 < n and 0 <= y - 1 and arr[x+1][y-1][0]: return True
    if 0 <= x - 1 and x + 1 < n and arr[x-1][y][1] and arr[x+1][y][1]: return True
    return False


def remove0(arr, x, y, n):
    # 제거 했을 때, 이어진 보 확인
    for dr, dc in (x - 1, y + 1), (x, y + 1):
        if 0 <= dc < n and 0 <= dr < n and arr[dr][dc][1]:
            if not check1(arr, dr, dc, n):
                return False

    # 제거 했을 때, 위 기둥 확인
    dc = y + 1
    if dc < n and arr[x][dc][0]:
        if not check0(arr, x, dc):
            return False
    return True


def remove1(arr, x, y, n):
    # 제거 했을 때, 양쪽 보 확인
    for dr, dc in (x - 1, y), (x + 1, y):
        if 0 <= dr < n and 0 <= dc < n and arr[dr][dc][1]:
            if not check1(arr, dr, dc, n):
                return False

    # 제거 했을 때, 이어진 기둥 확인
    for dr, dc in (x, y), (x + 1, y):
        if 0 <= dr < n and 0 <= dc < n and arr[dr][dc][0]:
            if not check0(arr, dr, dc):
                return False
    return True
