dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
# 사용하는 자료구조가 많음
def solution(board):
    N = len(board)
    answer = 0
    removed_cols = {}
    visited = [[0]*N for _ in range(N)]
    blocks_dict = {}
    cols_dict = {}
    fail_blocks = set()
    
    def get_block(block, start):
        nonlocal removed_cols, visited
        stack = [start]
        r1 = c1  = N
        r2 = c2 = 0
        coords = set()
        blocks_dict[block] = {'blocks': set(), 'empty': set()}
        while stack:
            r, c = stack.pop()
            for d in range(4):
                nr, nc = r+dr[d], c+dc[d]
                if 0<=nr<N and 0<=nc<N and not visited[nr][nc]:
                    if board[nr][nc] == block:
                        coords.add((nr, nc))
                        blocks_dict[block]['blocks'].add((nr, nc))
                        visited[nr][nc] = 1
                        r1, c1 = min(r1, nr), min(c1, nc)
                        r2, c2 = max(r2, nr), max(c2, nc)
                        if nc in cols_dict.keys():
                            cols_dict[nc].add(block)
                        else:
                            cols_dict[nc] = {block}
                        stack.append((nr, nc))
                        
        rectangle = set((i, j) for i in range(r1, r2+1) for j in range(c1, c2+1))
        empties = rectangle - coords
        for empty in empties:
            blocks_dict[block]['empty'].add(empty)
            if (empty[0]-1, empty[1]) in coords and block not in fail_blocks:
                fail_blocks.add(block)
                for coord in coords:
                    if coord[1] in removed_cols.keys():
                        removed_cols[coord[1]] = min(coord[0], removed_cols[coord[1]])
                    else:
                        removed_cols[coord[1]] = coord[0]
                
    
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            if board[i][j]:
                get_block(board[i][j], (i, j))
    
    while True:
        prev = set(fail_blocks)
        tmp_removed_cols = {}
        for col in removed_cols.keys():
            for block in cols_dict[col]:
                if block in fail_blocks:
                    continue
                for coord in blocks_dict[block]['empty']:
                    if coord[1] == col and coord[0] >= removed_cols[col]:
                        fail_blocks.add(block)
                        for tmp_coord in blocks_dict[block]['blocks']:
                            if tmp_coord[1] in tmp_removed_cols.keys():
                                tmp_removed_cols[tmp_coord[1]] = min(tmp_coord[0], tmp_removed_cols[tmp_coord[1]])
                            else:
                                tmp_removed_cols[tmp_coord[1]] = tmp_coord[0]
                        break
        if prev == fail_blocks:
            break
        for col in tmp_removed_cols.keys():
            removed_cols[col] = tmp_removed_cols[col]
    
    for block in blocks_dict.keys():
        if block not in fail_blocks:
            answer += 1
    
    
    return answer