from copy import deepcopy

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

answer = 0
cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctvs.append((i, j))
        if not board[i][j]:
            answer += 1

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

cctv_dict = {  # 보는 방향, 회전수 저장 
    1 : [[0, 0], 4],
    2 : [[0, 0], [2, 2], 2],
    3 : [[0, 0], [1, 1], 4],
    4 : [[0, 0], [1, 1], [2, 2], 4],
    5 : [[0, 0], [1, 1], [2, 2], [3, 3], 1]
}

def simulate(current_board, idx):
    global answer

    if idx == len(cctvs):
        unsupervised = 0
        for i in range(N):
            for j in range(M):
                if not current_board[i][j]:
                    unsupervised += 1
        answer = min(answer, unsupervised)
        return

    r, c = cctvs[idx]
    cctv = board[r][c]
    for d in range(cctv_dict[cctv][-1]):
        new_board = deepcopy(current_board)
        for dir in cctv_dict[cctv][:-1]:
            nr, nc = r, c
            while True:
                nr += dr[(dir[0]+d)%4]
                nc += dc[(dir[1]+d)%4]
                if not (0 <= nr < N) or not (0 <= nc < M):
                    break
                if board[nr][nc] == 6:
                    break
                if not board[nr][nc]:
                    new_board[nr][nc] = -1
        
        simulate(new_board, idx+1)

simulate(board, 0)
print(answer)


    