# 파괴되지 않은 건물
def solution(board, skill):
    answer = 0
    dp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for t, r1, c1, r2, c2, degree in skill:
        # 공격이면 -, 힐이면 +
        if t == 1:
            degree = -degree

        dp[r1][c1] += degree
        dp[r1][c2 + 1] += -degree
        dp[r2 + 1][c1] += -degree
        dp[r2 + 1][c2 + 1] += degree

    # 가로 누적합 계산
    for i in range(len(board)):
        for j in range(1, len(board[0])):
            dp[i][j] += dp[i][j - 1]

    # 세로 누적합 계산 하면서 파괴되지 않은 건물 찾기
    for i in range(len(board[0])):
        for j in range(1, len(board)):
            dp[j][i] = dp[j - 1][i] + dp[j][i]
            if board[j][i] + dp[j][i] > 0:
                answer += 1
    # 첫째줄은 따로
    for i in range(len(board[0])):
        if board[0][i] + dp[0][i] > 0:
            answer += 1

    return answer
