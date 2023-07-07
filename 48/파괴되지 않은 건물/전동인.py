def solution(board, skill):
    # 스킬의 종류에 따른 데미지
    type = {1: -1, 2: 1}

    # 보드의 행과 열의 개수
    n, m = len(board), len(board[0])

    # 데미지 배열 초기화
    demage = [[0]*m for _ in range(n)]

    # 모든 스킬에 대해 반복
    for s in skill:
        t, r1, c1, r2, c2, d = s
        d *= type[t]

        # 간선 누적 기법을 적용하여 데미지를 추가
        demage[r1][c1] += d
        if r2+1 < n and c2+1 < m:
            demage[r2+1][c2+1] += d
        if r2+1 < n:
            demage[r2+1][c1] -= d
        if c2+1 < m:
            demage[r1][c2+1] -= d

    # 파괴 되지 않은 건물 수
    cnt = 0

    # 생존 카운트
    for i in range(n):
        for j in range(m):
            # 간선 누적 기법을 이용하여 각 위치의 데미지를 계산
            if i > 0:
                demage[i][j] += demage[i-1][j]
            if j > 0:
                demage[i][j] += demage[i][j-1]
            if i > 0 and j > 0:
                demage[i][j] -= demage[i-1][j-1]

            # 파괴 되지 않았다면 카운트
            if board[i][j] + demage[i][j] > 0:
                cnt += 1

    return cnt
