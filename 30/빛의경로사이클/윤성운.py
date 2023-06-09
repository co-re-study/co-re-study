def solution(grid):
    
    # cycle 만들기
    def makeCycle(r, c, d):

        # 첫 좌표 기억
        initial_r = r
        initial_c = c
        initial_d = d
        acc = 0

        while True:
            acc += 1
            visited.add((r, c, d)) # 기록 남기기

            nr = r + direction_dict[grid[r][c]][d][0]
            nc = c + direction_dict[grid[r][c]][d][1]
            nd = direction_dict[grid[r][c]][d][2]

            # grid 벗어나면 좌표 조정
            if nr < 0:
                nr = len(grid) - 1
            elif nr == len(grid):
                nr = 0
            if nc < 0:
                nc = len(grid[0]) - 1
            elif nc == len(grid[0]):
                nc = 0

            if nr == initial_r and nc == initial_c and nd == initial_d:
                answer.append(acc)
                return

            r = nr
            c = nc
            d = nd

    # 0: 상, 1: 우, 2: 하, 3: 좌
    direction_dict = {
        "S": [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)],
        "L": [(0, -1, 3), (-1, 0, 0), (0, 1, 1), (1, 0, 2)],
        "R": [(0, 1, 1), (1, 0, 2), (0, -1, 3), (-1, 0, 0)]
    }

    # {(r1, c1, d1), (r2, c2, d2), ...}
    visited = set()

    answer = []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for d in range(4):
                if (r, c, d) not in visited:
                    makeCycle(r, c, d)

    answer.sort()

    return answer
