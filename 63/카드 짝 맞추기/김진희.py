from collections import deque


def solution(board, r, c):
    answer = cur(board, 0, r, c)  # 보드, 이동횟수, 현재 위치
    return answer


def cur(board, cnt, r, c):  # 보드, 이동횟수, 현재 위치
    # [1] 모든 카드를 찾는다
    lst = find_card(board, r, c)
    if not lst:
        return cnt

    n = 9999999
    for nr, nc, w in lst:
        table, acc, r, c = find_same(board, nr, nc)
        n = min(n, cur(table, cnt + w + acc, r, c))
    return n


def find_card(board, r, c):
    # 카드들 찾기
    cards = []
    q = deque([(r, c, 0)])
    visited = [[0] * 4 for _ in range(4)]
    while q:
        cr, cc, cnt = q.popleft()
        if visited[cr][cc] == 0:  # 방문하지 않은 곳이면
            visited[cr][cc] = 1
            if board[cr][cc]:     # 카드가 있으면
                cards.append((cr, cc, cnt + 1))
            for nr, nc in move(board, cr, cc):
                q.append((nr, nc, cnt + 1))
    return cards


def find_same(board, r, c):
    # 같은 카드 찾기
    table = [board[i][:] for i in range(4)]
    q = deque([(r, c, 0)])
    visited = [[0] * 4 for _ in range(4)]
    visited[r][c] = 1
    while q:
        cr, cc, cnt = q.popleft()
        for nr, nc in move(board, cr, cc):
            if visited[nr][nc] == 0:
                if board[nr][nc] == board[r][c]:
                    table[nr][nc] = 0
                    table[r][c] = 0
                    return table, cnt + 2, nr, nc
                q.append((nr, nc, cnt + 1))
                visited[nr][nc] = 1


def move(board, r, c):
    lst = []
    for dr, dc in (1, 0), (0, 1), (-1, 0), (0, -1):
        nr, nc = r + dr, c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            lst.append((nr, nc))
            while board[nr][nc] == 0:
                if not 0 <= nr + dr < 4 or not 0 <= nc + dc < 4:
                    lst.append((nr, nc))
                    break
                nr += dr
                nc += dc
            else:
                lst.append((nr, nc))
    return lst
