def turn_dist(direction, disk_num, time):
    time %= m
    if direction:  # 반시계
        arr[disk_num] = arr[disk_num][time:] + arr[disk_num][:time]
    else:
        arr[disk_num] = arr[disk_num][-time:] + arr[disk_num][:-time]


def dfs(center, x, y):
    global nums, flag

    stack = [(x, y)]
    visited = {(x, y)}
    while stack:
        cr, cc = stack.pop()
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = cr + dr, cc + dc
            # 범위 바깥이면 바깥 애를 확인해야함
            # if nr == n:
            #     nr = 0
            # elif nr == -1:
            #     nr = n - 1
            if nc == m:
                nc = 0
            elif nc == -1:
                nc = m - 1
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] not in visited:
                if arr[nr][nc] == center:
                    arr[nr][nc] = 0
                    stack.append((nr, nc))
                    visited.add((nr, nc))
    if len(visited) > 1:
        arr[x][y] = 0
        flag = 0
        nums -= len(visited)


n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
nums = n * m  # 원판에 몇 개의 수가 있나 -> 평균 낼 때 사용

for tc in range(t):
    xi, di, ki = map(int, input().split())  # 배수, 방향, 회전 수
    # [1] xi의 배수에 해당하는 원판을 회전
    for disk in range(1, (n // xi) + 1):
        target = disk * xi - 1
        turn_dist(di, target, ki)

    # [2] 인접한 같은 수 있으면 삭제
    flag = 1  # 같은 수 없음
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                dfs(arr[i][j], i, j)

    # [3] 같은 수 없었다면 원판의 평균 기준 +- 1
    if flag:
        # 모든 원소가 삭제당했다면?
        if not nums:
            print(0)
            exit(0)
        sum_disk = 0
        for i in range(n):
            sum_disk += sum(arr[i])
        sum_disk /= nums
        for i in range(n):
            for j in range(m):
                if arr[i][j]:  # 0이 아닐때만 계산
                    if arr[i][j] > sum_disk:
                        arr[i][j] -= 1
                    elif arr[i][j] < sum_disk:
                        arr[i][j] += 1

# [4] 턴 종료 후 원판 수의 합
answer = sum(arr[0])
for i in range(1, n):
    answer += sum(arr[i])

print(answer)
