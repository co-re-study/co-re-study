from copy import deepcopy


def dfs(arr, num):
    global ans
    if num == len(cctv):
        count = 0
        for i in range(N):
            for j in range(M):
                if not arr[i][j]:
                    count += 1
        ans = min(ans, count)
        return
    target = deepcopy(arr)
    x, y, n = cctv[num]
    for dir in cctv_dir[n]:
        for d in dir:
            x0, y0 = x, y
            while True:
                x0 += dx[d]
                y0 += dy[d]
                if x0 < 0 or x0 >= N or y0 < 0 or y0 >= M or target[x0][y0] == 6:
                    break
                if not target[x0][y0]:
                    target[x0][y0] = -1
        dfs(target, num+1)
        target = deepcopy(arr)


cctv_dir = {1: [[0], [1], [2], [3]],
            2: [[0, 2], [1, 3]],
            3: [[0, 1], [1, 2], [2, 3], [3, 0]],
            4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
            5: [[0, 1, 2, 3]]}
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = []
cctv = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if 0 < arr[i][j] < 6:
            cctv.append([i, j, arr[i][j]])
ans = 64
dfs(arr, 0)
print(ans)
