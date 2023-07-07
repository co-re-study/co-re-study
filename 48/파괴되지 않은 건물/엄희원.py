def solution(board, skill):
    answer = 0

    acc = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for s in skill:
        if s[0] == 1:
            acc[s[1]][s[2]] += -s[-1]
            acc[s[1]][s[4] + 1] += s[-1]
            acc[s[3] + 1][s[2]] += s[-1]
            acc[s[3] + 1][s[4] + 1] += -s[-1]
        else:
            acc[s[1]][s[2]] += s[-1]
            acc[s[1]][s[4] + 1] += -s[-1]
            acc[s[3] + 1][s[2]] += -s[-1]
            acc[s[3] + 1][s[4] + 1] += s[-1]

    for i in range(len(acc)):
        for j in range(1, len(acc[0])):
            acc[i][j] += acc[i][j - 1]

    for j in range(len(acc[0])):
        for i in range(1, len(acc)):
            acc[i][j] += acc[i - 1][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + acc[i][j] >= 1:
                answer += 1

    return answer

print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))