# 각 칸마다 SL R격자
def solution(grid):
    answer = []
    #델타탐색 정의
    delta_x = [0,1,0,-1]
    delta_y = [-1,0,1,0]

    # grid기반으로 격자 그리자
    visited = [[[False] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid)) ]

    #각 요소에서 출발
    for i2 in range(len(grid)):
        for i3 in range(len(grid[0])):
            for d in range(4):
                if visited[i2][i3][d]:
                    continue
                cnt = 0
                r = i2
                c = i3
                while not visited[i2][i3][d]:
                    visited[i2][i3][d] = True
                    cnt += 1
                    if grid[r][c] == "S":
                        pass
                    elif grid[r][c] == "R":
                        d = (d+1)%4
                    elif grid[r][c] == "L":
                        d = (d-1)%4
                    r = (r+delta_y[d])%len(grid)
                    c = (c+delta_x[d])%len(grid[0])
                answer.append(cnt)
    answer = sorted(answer)
    return answer


grid1  = ["SL","LR"]
grid2 = ["S"]

print(solution(grid1))