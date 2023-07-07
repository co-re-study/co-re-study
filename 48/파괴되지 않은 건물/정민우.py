def solution(board, skills):
    n, m, answer = len(board), len(board[0]), 0
    print(n, m, answer)
    skill_board = [[0] * (m + 1) for _ in range(n + 1)]
    for type, r1, c1, r2, c2, degree in skills:
        if type == 1:
            degree *= -1
        skill_board[r1][c1] += degree
        skill_board[r1][c2 + 1] -= degree
        skill_board[r2 + 1][c1] -= degree
        skill_board[r2 + 1][c2 + 1] += degree
    for r in range(n + 1):
        acc = 0
        for c in range(m + 1):
            acc += skill_board[r][c]
            skill_board[r][c] = acc
    for c in range(m + 1):
        acc = 0
        for r in range(n + 1):
            acc += skill_board[r][c]
            skill_board[r][c] = acc
    for i in range(n):
        for j in range(m):
            board[i][j] += skill_board[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer