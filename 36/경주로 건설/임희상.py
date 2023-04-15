import copy
def solution(board):
    answer = 0
    N = len(board)
    dp = [[0] * N for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    stack = []
    if not board[0][1]:
        stack.append([0, 1, 0, 100, {(0, 0)}])
    if not board[1][0]:
        stack.append([1, 0, 1, 100, {(0, 0)}])
    # [r, c, prev_direction, cost]
    while stack:
        r, c, prev_d, cost, log_set = stack.pop()
        if dp[r][c]:
            dp[r][c] = min(cost, dp[r][c])
        else:
            dp[r][c] = cost
        new_log = set(log_set)
        new_log.add((r, c))
        for d in range(4):
            if 0<=r+dr[d]<N and 0<=c+dc[d]<N and not board[r+dr[d]][c+dc[d]] and (r+dr[d], c+dc[d]) not in new_log:
                if (prev_d+d)%2:
                    new_cost = cost + 600
                else:
                    new_cost = cost + 100
                if dp[r+dr[d]][c+dc[d]] >= new_cost - 400 or not dp[r+dr[d]][c+dc[d]]:
                    stack.append([r+dr[d], c+dc[d], d, new_cost, new_log])
    answer = dp[-1][-1]
    return answer