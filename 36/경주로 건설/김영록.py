from heapq import heappop, heappush


def solution(board):
    N = len(board)
    # 값을 갱신해줄 것이니 가장 큰 값으로 설정해준다. 
    # for _ in range(4)는 각 방향에서 어떤 값을 가지는지 알고 싶기 때문.
    costs = [[[987654321]*N for _ in range(N)] for _ in range(4)]
    # 초기 방향을 정한다 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
    d_info = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
    # 초기좌표 (0,0) 에서는 오른쪽, 아래쪽으로만 이동할 수 있기 때문에
    # 초기값을 이렇게 설정해주었다.
    queue = [[0, 0, 0, 0], [0, 0, 1, 0]]
    while queue:
        x, y, d, c = heappop(queue)
        for dd in d_info:
            dx, dy = d_info[dd]
            x1, y1 = x+dx, y+dy
            if 0 <= x1 < N and 0 <= y1 < N and not board[x1][y1]:
                temp = c + (100 if d == dd else 600)
                if temp < costs[dd][x1][y1]:
                    costs[dd][x1][y1] = temp
                    heappush(queue, [x1, y1, dd, temp])
    answer = min(costs[i][N-1][N-1] for i in range(4))
    return answer
