def solution(board, skill):
    x = len(board)
    y = len(board[0])
    arr = [[0]*(y+1) for _ in range(x+1)]
    answer = 0
    for type, r1, c1, r2, c2, degree in skill:
        arr[r1][c1] += degree if type == 2 else -degree
        arr[r1][c2+1] -= degree if type == 2 else -degree
        arr[r2+1][c1] -= degree if type == 2 else -degree
        arr[r2+1][c2+1] += degree if type == 2 else -degree
    for i in range(x):
        for j in range(y):
            arr[i][j+1] += arr[i][j]
    for j in range(y):
        for i in range(x):
            arr[i+1][j] += arr[i][j]
    for i in range(x):
        for j in range(y):
            board[i][j] += arr[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [
      [1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [
      [1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
