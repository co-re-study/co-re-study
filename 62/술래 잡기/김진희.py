'''
- 밖에 snail배열을 두고 술래 이동시킬 때 사용
- 도망자 이동시
    도망자를 하나씩 꺼내서 거리 확인하고 이동시키되, arr[i][j].remove()하고 갈지
    술래로부터 3칸 이내를 돌면서 pop해서 위치 찾아서 이동시킬지
    일단 전자로
'''
N, M, H, K = map(int, input().split())
players = {}
arr = [[[] for _ in range(N)] for _ in range(N)]
for idx in range(1, M+1):
    X, Y, D = map(lambda x: int(x) - 1, input().split())
    players[idx] = [X, Y, D]
    arr[X][Y].append(idx)

trees = set()
for _ in range(H):
    X, Y = map(lambda x: int(x) - 1, input().split())
    trees.add((X, Y))

di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)  # 우 하 좌 상
alive = [1] * (M+1)  # 죽으면 0으로 만들자
alive[0] = 0

middle = N//2
R, C, D = middle, middle, 3
snail = [[0] * N for _ in range(N)]
snail[R][C] = 1
look = 1  # 1 : 0번 방향이 0이면 방향 +1 / 0 : 한 칸 앞이 0이면 방향 -1

answer = 0
for tc in range(1, K + 1):
    if sum(alive) == 0:  # 턴이 끝나기 전에 도망자를 다 잡았으면
        break
    # [1] 술래와의 거리가 3 이하인 도망자 이동
    for player in players:
        if alive[player]:
            cr, cc, d = players[player]
            if abs(R-cr) + abs(C-cc) <= 3:
                if not 0 <= cr + di[d] < N or not 0 <= cc + dj[d] < N:
                    d = (d + 2) % 4
                nr, nc = cr + di[d], cc + dj[d]
                if (nr, nc) != (R, C):
                    # 현재 arr에서 삭제
                    arr[cr][cc].remove(player)
                    # 다음 arr에 추가
                    arr[nr][nc].append(player)
                    # info 변경
                    players[player] = [nr, nc, d]
                else:
                    players[player][2] = d

    # [2] 술래 이동
    # 앞으로 한 칸 가
    R += di[D]
    C += dj[D]
    if look:  # 정방향
        # snail 찍어
        snail[R][C] = 1
        # 오른쪽이 0이면 방향 꺾어
        nd = (D + 1) % 4
        if snail[R + di[nd]][C + dj[nd]] == 0:
            D = nd
        # 0, 0에 도착했으면 방향 아래로
        if (R, C) == (0, 0):
            D = 1
            snail[R][C] = 0  # 시작점 0으로 돌리고
            look = 0  # 역방향이다 선언
    else:
        # snail 0으로 돌려
        snail[R][C] = 0
        # 한 칸 더 앞이 범위 밖이거나 0이면 방향 -1
        if not 0 <= R+di[D] < N or not 0 <= C + dj[D] < N or snail[R+di[D]][C+dj[D]] == 0:
            D = (D - 1) % 4
        # 가운데 도착했으면 방향 위로
        if (R, C) == (middle, middle):
            D = 3
            snail[R][C] = 1
            look = 1

    # [3] 잡기
    for k in range(3):
        nr, nc = R + di[D] * k, C+dj[D]*k
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] and (nr, nc) not in trees:
            cnt = len(arr[nr][nc])
            answer += tc * cnt
            for runner in range(cnt):
                alive[arr[nr][nc].pop()] = 0

print(answer)