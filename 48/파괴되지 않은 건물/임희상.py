def solution(board, skill):
    N, M = len(board), len(board[0])
    answer = 0
    prefix = [[0] * (M + 2) for _ in range(N + 2)]  # 패딩
    diff = [[0] * M for _ in range(N)]
    for current in skill:
        t, r1, c1, r2, c2, d = current
        if t == 1:
            d = -d
        prefix[r1][c1] += d
        prefix[r2 + 1][c2 + 1] += d
        prefix[r2 + 1][c1] -= d
        prefix[r1][c2 + 1] -= d
    
    
    for r in range(N):
        for c in range(M):
            diff[r][c] = prefix[r][c]

    for r in range(1, N):
        for c in range(M):
            diff[r][c] = diff[r - 1][c] + diff[r][c]

    for r in range(N):
        for c in range(1, M):
            diff[r][c] = diff[r][c - 1] + diff[r][c]

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] + diff[r][c] > 0:
                answer += 1

    return answer
