from itertools import permutations
from collections import deque
# 이건 할거
def solution(board, r, c):
    
    def dfs(card_idx, target_r, target_c, r, c, acc, turn):
        nonlocal answer
        
        if acc >= answer:
            return
        
        if card_idx == len(cards):
            answer = min(answer, acc)
            return
        
        queue = deque([(r, c, 1)])
        visited = [[0] * n for _ in range(n)]
        visited[r][c] = 1
        
        if r == target_r and c == target_c:
            queue.clear()
            acc += 1
            
        while queue:
            cr, cc, dist = queue.popleft()
            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    if nr == target_r and nc == target_c:
                        queue.clear()
                        acc += dist + 1
                        r, c = nr, nc
                        break
                    visited[nr][nc] = 1
                    queue.append((nr, nc, dist + 1))
                
                flag = False
                k = 1
                while True:
                    nr = cr + dr[i] * k
                    nc = cc + dc[i] * k
                    if nr < 0 or nr >= n or nc < 0 or nc >= n:
                        if not visited[nr - dr[i]][nc - dc[i]]:
                            visited[nr - dr[i]][nc - dc[i]] = 1
                            queue.append((nr - dr[i], nc - dc[i], dist + 1))
                        break
                    if nr == target_r and nc == target_c:
                        acc += dist + 1
                        r, c = nr, nc
                        flag = True
                        queue.clear()
                        break
                    if board[nr][nc]:
                        if not visited[nr][nc]:
                            visited[nr][nc] = 1
                            queue.append((nr, nc, dist + 1))
                        break
                    k += 1
                if flag:
                    break
                    
        if not turn:
            for i in range(2):
                if cards[perm[card_idx]][i] != (target_r, target_c):
                    dfs(card_idx, cards[perm[card_idx]][i][0], cards[perm[card_idx]][i][1], r, c, acc, 1)
        else:
            for i in range(2):
                board[cards[perm[card_idx]][i][0]][cards[perm[card_idx]][i][1]] = 0
            if card_idx + 1 == len(cards):
                dfs(card_idx + 1, 0, 0, r, c, acc, 0)
            else:
                for i in range(2):
                    dfs(card_idx + 1, cards[perm[card_idx + 1]][i][0], cards[perm[card_idx + 1]][i][1], r, c, acc, 0)
            for i in range(2):
                board[cards[perm[card_idx]][i][0]][cards[perm[card_idx]][i][1]] = perm[card_idx]
                    
    
    n = 4
    cards = dict()
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                if board[i][j] in cards:
                    cards[board[i][j]].append((i, j))
                else:
                    cards[board[i][j]] = [(i, j)]
                    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
                    
    answer = 987654321
    for perm in permutations(cards.keys(), len(cards)):
        for i in range(2):
            dfs(0, cards[perm[0]][i][0], cards[perm[0]][i][1], r, c, 0, 0)
                
    return answer