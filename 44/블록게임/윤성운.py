def solution(board):
    
    # 블록 놓을 수 있는 칸 찾기
    def find_max_heights():
        for c in range(N):
            for r in range(N):
                if board[r][c]:
                    max_heights[c] = r - 1
                    break
            else:
                max_heights[c] = N - 1
    
    
    # 블록 쌓기
    def pile_blocks():
        # 쌓인 블록 위치 저장
        positions = []
        for c in range(N):
            # 현재 놓을 수 있는 블록이 있으면 블록 놓기
            if max_heights[c] >= 0:
                board[max_heights[c]][c] = -1
                positions.append((max_heights[c], c))
                max_heights[c] -= 1
                continue
                    
        return positions
    

    # 직사각형인지 확인
    def check_rectangle(nr, nc, range_r, range_c):
        nonlocal answer
        
        tmp = set()
        cnt = 0
        for r in range(range_r):
            for c in range(range_c):
                if not board[nr + r][nc + c]:
                    return
                if board[nr + r][nc + c] != -1:
                    cnt += 1
                tmp.add(board[nr + r][nc + c])
        if len(tmp) == 2 and cnt == 4:
            answer += 1
            for r in range(range_r):
                for c in range(range_c):
                    board[nr + r][nc + c] = 0
            return True


    # 쌓인 블록 위치에 대해서 직사각형이 가능한지 확인
    def check_piled_blocks():
        flag = False
        for position in positions:
            if position[0] + 1 < N:
                if position[1] - 2 >= 0:
                    if check_rectangle(position[0], position[1] - 2, 2, 3):
                        flag = True
                if position[1] - 1 >= 0 and position[1] + 1 < N:
                    if check_rectangle(position[0], position[1] - 1, 2, 3):
                        flag = True
                if position[1] + 2 < N:
                    if check_rectangle(position[0], position[1], 2, 3):
                        flag = True
            if position[0] + 2 < N:
                if position[1] - 1 >= 0:
                    if check_rectangle(position[0], position[1] - 1, 3, 2):
                        flag = True
                if position[1] + 1 < N:
                    if check_rectangle(position[0], position[1], 3, 2):
                        flag = True
        if flag:
            return True
        return False
               
    
    # 빈공간 있다면 블록 내리기
    def drop_blocks():
        positions = []
        for c in range(N):
            for r in range(N - 1, -1 , -1):
                # 검은 블록을 만났다면
                if board[r][c] == -1:
                    point = r
                    # 해당 블록을 떨어뜨릴 수 있는 가장 밑 위치 구하기
                    for next_r in range(r + 1, N):
                        if board[next_r][c]:
                            break
                        point = next_r
                    # 찾은 검은 블록부터 위 블록 모두 떨어뜨리기
                    for above_r in range(r, -1, -1):
                        if board[above_r][c] == -1:
                            board[above_r][c] = 0
                            board[point][c] = -1
                            positions.append((point, c))
                            point -= 1
                    break
        return positions
                    
    
    N = len(board)
    max_heights = [-1] * N
                
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    answer = 0
    while True:
        find_max_heights() # 떨어뜨릴 위치 구하기
        positions = pile_blocks() # 블록 떨어뜨리고 떨어뜨린 위치 저장
        while check_piled_blocks(): # 직사각형을 찾았다면
            positions = drop_blocks() # 빈공간 없애기
        
        # 검은블록을 맨 위까지 모두 채웠다면 종료
        for c in range(N):
            if not board[0][c]:
                break
        else:
            break

    return answer