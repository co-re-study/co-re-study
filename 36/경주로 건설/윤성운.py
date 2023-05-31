import heapq

def solution(board):
    INF = 987654321
    distance = [[INF] * len(board) for _ in range(len(board))]
    distance[0][0] = 0
    
    def dijk():
        queue = [(0, 0, 0, 0)]
        visited = set()
        
        while queue:
            # direction: 위아래 방향이면 0, 좌우 방향이면 1
            cost, r, c, direction = heapq.heappop(queue)
            if cost > distance[r][c] + 300:
                continue

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < len(board) and 0 <= nc < len(board) and not board[nr][nc]:
                    # 이전 방향과 같은 경우
                    if (r, c) == (0, 0) or direction == i % 2:
                        next_cost = 100
                    # 이전 방향과 다른 경우
                    else:
                        next_cost = 600
                    if cost + next_cost <= distance[nr][nc] + 300:
                        if cost + next_cost <= distance[nr][nc]:
                            distance[nr][nc] = cost + next_cost
                        heapq.heappush(queue, (cost + next_cost, nr, nc, i % 2))
            
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    dijk()

    return distance[-1][-1]