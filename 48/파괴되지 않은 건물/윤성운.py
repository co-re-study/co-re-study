def solution(board, skill):
    
    # 네 점 찍기
    acc_arr = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for s in skill:
        [t, r1, c1, r2, c2, degree] = s
        degree = degree if t == 2 else -degree
        acc_arr[r1][c1] += degree
        acc_arr[r1][c2 + 1] -= degree
        acc_arr[r2 + 1][c1] -= degree
        acc_arr[r2 + 1][c2 + 1] += degree
        
    # 좌 -> 우로 누적합
    for r in range(len(board) + 1):
        for c in range(1, len(board[0]) + 1):
            acc_arr[r][c] += acc_arr[r][c - 1]
    
    # 상 -> 하로 누적합
    for c in range(len(board[0]) + 1):
        for r in range(1, len(board) + 1):
            acc_arr[r][c] += acc_arr[r - 1][c]
    
    # 정답구하기
    answer = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] + acc_arr[r][c] > 0:
                answer += 1

    return answer