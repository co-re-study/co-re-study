def solution(grid):
    answer = []
    R = len(grid)
    C = len(grid[0])
    # 모든 방향으로 빛이 나가야 모든 사이클을 찾았다고 할 수 있음
    board = [[[0, 0, 0, 0] for _ in range(C)] for _ in range(R)]
    for row in grid:
        row = list(grid)
    print(board)
    def find_cycle(r, c, d):
        nonlocal board
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        start = current = [r, c, d]
        cycle = 0
        while start != current or not cycle:
            cycle += 1
            nr, nc, nd = current
            print(current, nd)
            board[nr][nc][nd] = 1
            nr += dr[nd]
            nr %= R
            if nr == -1:
                nr = R-1
            nc += dc[nd]
            nc %= C
            if nc == -1:
                nc = C-1
            if grid[nr][nc] == 'L':
                nd -= 1
                nd %= 4
            if grid[nr][nc] == 'R':
                nd += 1
                nd %= 4
            current = [nr, nc, nd]
        return cycle

    for i in range(R):
        for j in range(C):
            for d in range(4):
                if not board[i][j][d]:
                    cycle_length = find_cycle(i, j, d)
                    answer.append(cycle_length)
                print(board)

    print(answer)
    return answer

solution(["S", "S"])