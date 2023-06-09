
# 처음에 어차피 0,0에서만 4방향으로 쏘면 알아서 사이클이 만들어 질 줄 알았는데,
# 모든 격자에서 모든 방향으로 쏴줘야 맞는다.
# 0,0에서만 4방향으로 쏘는 것만 체크했을 때도 테스트케이스는 다 맞는다.
# 테스트케이스는 맞는데, 채점할 때 다 틀리는 경우에는 0,0에서만 4방향으로 쏘는게 아니라
# 모든 격자에서 4방향으로 다 쏘는 로직으로 변경해줘야함.
# 이거 때문에 시간 너무 많이 쏟음.. ㅠㅠ

def solution(grid):
    rl = len(grid)
    cl = len(grid[0])
    left_dict = {1:3, 2:4, 3:2, 4:1}
    right_dict = {1:4, 2:3, 3:1, 4:2}
    # 0: 제자리 1: 상 2: 하 3: 좌 4: 우
    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]
    answer = []
    dict_setting = dict()
    for i in range(rl):
        for j in range(cl):
            dict_setting[(i, j)] = set()
    for r in range(rl):
        for c in range(cl):
            for i in range(1, 5):
                x, y = r, c
                dx = x + dr[i]
                dy = y + dc[i]
                direction = i
                # if direction not in dict_setting[(0, 0)]:
                #     dict_setting[(0, 0)].add(direction)
                # else:
                #     continue
                cycle = 0
                while True:
                    if dx < 0:
                        dx = rl -1
                    elif dx > rl-1:
                        dx = 0

                    if dy < 0:
                        dy = cl -1
                    elif dy > cl - 1:
                        dy = 0


                    if grid[dx][dy] == 'L':
                        direction = left_dict[direction]
                    elif grid[dx][dy] == 'R':
                        direction = right_dict[direction]

                    if direction in dict_setting[(dx, dy)]:
                        if cycle == 0:
                            pass
                        else:
                            answer.append(cycle)
                        break
                    dict_setting[(dx, dy)].add(direction)
                    dx = dx + dr[direction]
                    dy = dy + dc[direction]
                    cycle += 1
    answer.sort()
    return answer

grid1 = ["SL", "LR"]
grid2 = ["S"]
grid3 = ["R", "R"]
grid4 = ["RLS","SLR"] # [12, 12]
print(solution(grid4))
