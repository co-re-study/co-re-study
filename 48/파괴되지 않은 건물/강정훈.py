# 1차시도 역시 정확성은 통과하는데, 효율성에서 통과하지 못함.
# skill들을 돌떄마다 이중 포문을 돌리는게 아니라 skill들을 이미 다 돌려 놓고 이중포문 돌리는 형식으로 해야 통과될듯
# def solution(board, skill):
#     answer = 0
#     for i in range(len(skill)):
#         skill_type, r1, c1, r2, c2, degree = skill[i][0], skill[i][1], skill[i][2], skill[i][3], skill[i][4], skill[i][5]
#         for j in range(r2+1-r1):
#             for k in range(c2+1-c1):
#                 if skill_type == 1:
#                     board[r1+j][c1+k] -= degree
#                 else:
#                     board[r1+j][c1+k] += degree
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] >=1 :
#                 answer += 1
#
#     return answer

def solution(board, skill):
    answer = 0
    accumulated_arr = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    for i in range(len(skill)):
        skill_type, r1, c1, r2, c2, degree = skill[i][0], skill[i][1], skill[i][2], skill[i][3], skill[i][4], skill[i][5]
        if skill_type == 1:
            accumulated_arr[r1][c1] -= degree
            accumulated_arr[r1][c2+1] += degree
            accumulated_arr[r2+1][c1] += degree
            accumulated_arr[r2+1][c2+1] -= degree
        else:
            accumulated_arr[r1][c1] += degree
            accumulated_arr[r1][c2 + 1] -= degree
            accumulated_arr[r2 + 1][c1] -= degree
            accumulated_arr[r2 + 1][c2 + 1] += degree
    for i in range(len(board)):
        for j in range(len(board[0])):
            accumulated_arr[i][j+1] += accumulated_arr[i][j]
    for i in range(len(board[0])):
        for j in range(len(board)):
            accumulated_arr[j+1][i] += accumulated_arr[j][i]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += accumulated_arr[i][j]
            if board[i][j] >= 1:
                answer += 1


    return answer



print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))