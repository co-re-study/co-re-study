dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m, h, k = map(int, input().split())
# n*n, m-fugitive, h-tree, k-repeat
# 도망자가 먼저, 다음 술래 - 1턴
# 술래와의 거리가 3 이하인 도망자만 움직인다
# 만약 가려는 칸에 술래가 있다면 움직이지 않음
# 벽에 부딪히면 반대로 틀어서 움직임 (술래가 있다면 움직이지 않음)
# 술래는 가운데에서 달팽이 모양으로
# 술래는 바라보고 있는 방향 기준 3칸 (나무가 있는 칸은 생각x)
# 도망자는 잡히면 없어지고 (n번째턴)*(현재턴에 잡힌 도망자) 점수 획득
fugitives = []
for _ in range(m):  # fugitive, d: 1-좌우, 2-상하
    fx, fy, d = map(int, input().split())
    fugitives.append((fx-1, fy-1, d))
trees = []
for _ in range(h):  # tree
    tx, ty = map(int, input().split())
    trees.append((tx-1, ty-1))
x0, y0, d0 = n//2, n//2, 0  # 술래 정보
counter = False  # 끝에 도달했을 때 다시 가운데로 돌아와야 함
move_dist = 1
target = 0  # 1 1 2 2 3 3 ..식으로 움직이므로 2일 때 늘린다
move_cnt = 0
ans = 0
for turn in range(1, k+1):
    # 도망자 이동
    for i in range(len(fugitives)):
        fx0, fy0, fd = fugitives[i]  # 도망자 정보
        dist = abs(fx0-x0)+abs(fy0-y0)  # 술래와의 거리
        if dist <= 3:
            fx1 = fx0+dx[fd]
            fy1 = fy0+dy[fd]
            if 0 <= fx1 < n and 0 <= fy1 < n:
                if (fx1, fy1) != (x0, y0):
                    fugitives[i] = (fx1, fy1, fd)
            else:
                fd1 = (fd+2) % 4
                fx1 = fx0+dx[fd1]
                fy1 = fy0+dy[fd1]
                if 0 <= fx1 < n and 0 <= fy1 < n:
                    if (fx1, fy1) != (x0, y0):
                        fugitives[i] = (fx1, fy1, fd1)
    # 술래 이동
    x0 += dx[d0]
    y0 += dy[d0]
    target += 1
    if not counter:
        if target == move_dist:
            target = 0
            move_cnt += 1
            if move_cnt < 2*(n-1) and not move_cnt % 2:
                move_dist += 1
            if move_cnt == 2*n-1:
                counter = True
                d0 = 2
                move_cnt = 0
            else:
                d0 = (d0+1) % 4
    else:
        if target == move_dist:
            target = 0
            move_cnt += 1
            if 1 < move_cnt and move_cnt % 2:
                move_dist -= 1
            if move_cnt == 2*n-1:
                counter = False
                d0 = 0
                move_dist = 1
                move_cnt = 0
            else:
                d0 = (d0-1) % 4
    # print(x0, y0, move_dist, move_cnt)
    # 도망자 잡기
    vision = []
    arrest = []
    for j in range(3):
        x1 = x0+dx[d0]*j
        y1 = y0+dy[d0]*j
        if (x1, y1) in trees:
            continue
        if 0 <= x1 < n and 0 <= y1 < n:
            vision.append((x1, y1))
    for fxx, fyy, fdd in fugitives:
        if (fxx, fyy) in vision:
            arrest.append((fxx, fyy, fdd))
    ans += turn*len(arrest)
    for ax, ay, ad in arrest:
        idx = fugitives.index((ax, ay, ad))
        fugitives.pop(idx)
print(ans)
# 누가 이거 냈어......