dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [0, 3], [
    1, 2], [1, 3]], [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], [[0, 1, 2, 3]]]


def fill(x, y, arr, d):
    for i in d:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 6:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = '#'
            else:
                break


def dfs(arr, cnt):
    global ans
    temp = [i[:] for i in arr]
    if cnt == cctv_cnt:
        num = 0
        for i in range(n):
            num += temp[i].count(0)
        ans = min(ans, num)
        return
    x, y, cctv = q[cnt]
    for i in direction[cctv]:
        fill(x, y, temp, i)
        dfs(temp, cnt + 1)
        temp = [i[:] for i in arr]


n, m = map(int, input().split())
s = []
q = []
cctv_cnt = 0
ans = float('inf')
for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
    for j in range(len(a)):
        if a[j] not in [0, 6]:
            q.append([i, j, a[j]])
            cctv_cnt += 1
dfs(s, 0)
print(ans)
