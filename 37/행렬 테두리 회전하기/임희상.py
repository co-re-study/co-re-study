from collections import deque
def solution(rows, columns, queries):
    answer = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    board = [[0]*columns for _ in range(rows)]
    original = [[0]*columns for _ in range(rows)]
    for r in range(rows):
        for c in range(columns):
            board[r][c] = r*columns + c + 1
            original[r][c] = r*columns + c + 1
            
    for query in queries:
        x1, y1, x2, y2 = query
        r, c = x1 - 1, y1 - 1
        x, y = x2 - x1, y2 - y1
        queue = deque([])
        coord_queue = deque([])
        min_val = rows * columns
        d = 0
        for _ in range(y):
            c += dc[d]
            if board[r][c] < min_val:
                min_val = board[r][c]
            queue.append(board[r][c])
            coord_queue.append((r, c))
        d = 1
        for _ in range(x):
            r += dr[d]
            if board[r][c] < min_val:
                min_val = board[r][c]
            queue.append(board[r][c])
            coord_queue.append((r, c))
        d = 2
        for _ in range(y):
            c += dc[d]
            if board[r][c] < min_val:
                min_val = board[r][c]
            queue.append(board[r][c])
            coord_queue.append((r, c))
        d = 3
        for _ in range(x):
            r += dr[d]
            if board[r][c] < min_val:
                min_val = board[r][c]
            queue.append(board[r][c])
            coord_queue.append((r, c))
        coord_queue.append(coord_queue.popleft())
        answer.append(min_val)
        while queue:
            r, c = coord_queue.popleft()
            board[r][c] = queue.popleft()
    
    
    return answer