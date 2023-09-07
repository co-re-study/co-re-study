def solution(grid, d, k):
    
    N = len(grid)
    M = len(grid[0])
    D = len(d)
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    path_dict = dict()

    for cr in range(N):
        for cc in range(M):
            visited = [[[0] * (D + 1) for _ in range(M)] for _ in range(N)]
            visited[cr][cc][0] = 1
            
            # 경사로를 따라가면서 방문 수 누적
            for i in range(1, D + 1):
                for r in range(N):
                    for c in range(M):
                        if not visited[r][c][i - 1]:
                            continue
                        for j in range(4):
                            nr = r + dr[j]
                            nc = c + dc[j]
                            if 0 <= nr < N and 0 <= nc < M and  grid[nr][nc] - grid[r][c] == d[i - 1]:
                                visited[nr][nc][i] = (visited[nr][nc][i] + visited[r][c][i - 1]) % 1000000007
            
            # 누적된 방문 수 저장
            path_dict[(cr, cc)] = dict()
            for r in range(N):
                for c in range(M):
                    if visited[r][c][-1]:
                        path_dict[(cr, cc)][(r, c)] = visited[r][c][-1]

    # 2^power만큼 사이클을 돌았을 때 도달하는 좌표 정보와 방문 수 저장
    dp = [dict() for _ in range(31)]
    for position in path_dict:
        dp[0][position] = dict()
        for dest in path_dict[position]:
            dp[0][position][dest] = path_dict[position][dest]
    
    for power in range(1, 31):
        for current in dp[power - 1]:
            dp[power][current] = dict()
            for mid in dp[power - 1][current]:
                if mid in dp[power - 1]:
                    for dest in dp[power - 1][mid]: 
                        if dest in dp[power][current]:
                            dp[power][current][dest] = (dp[power][current][dest] + dp[power - 1][current][mid] * dp[power - 1][mid][dest]) % 1000000007
                        else:
                            dp[power][current][dest] = (dp[power - 1][current][mid] * dp[power - 1][mid][dest]) % 1000000007
    
    # 가장 처음으로 사이클을 시작하는 좌표 저장
    acc_dict = dict()
    for position in path_dict:
        if not path_dict[position]:
            continue
        acc_dict[position] = 1
    
    # 2^power만큼 건너뛰면서 방문 가능한 수 누적
    cycle = 0
    power = 30
    while cycle != k:
        while cycle + (1 << power) > k:
            power -= 1
        cycle += 1 << power
        new_acc_dict = dict()
        for current in acc_dict:
            for dest in dp[power][current]:
                if dest in new_acc_dict:
                    new_acc_dict[dest] = (new_acc_dict[dest] + (acc_dict[current] * dp[power][current][dest])) % 1000000007
                else:
                    new_acc_dict[dest] = (acc_dict[current] * dp[power][current][dest]) % 1000000007
        acc_dict = new_acc_dict
    
    # 가장 마지막에 도달한 값들 더해서 출력
    answer = 0
    for position in acc_dict:
        answer = (answer + acc_dict[position]) % 1000000007
    
    return answer