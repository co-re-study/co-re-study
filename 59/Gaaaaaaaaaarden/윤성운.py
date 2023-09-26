import sys
from collections import deque
input = sys.stdin.readline

# status : 0(배양액 뿌릴 지역 선택), 1(선택된 지역 중 초록색 배양액 뿌릴 지역 선택)
def comb(sidx, idx, selection, arr, status):
    global answer

    if sidx == len(selection):
        if not status:
            green_positions = [0] * G
            comb(0, 0, green_positions, selection, 1)
            return
        
        new_arr = [[0] * M for _ in range(N)]
        queue = deque()
        for r in range(N):
            for c in range(M):
                if garden[r][c]:
                    new_arr[r][c] = 1
        for position in selection:
            new_arr[position[0]][position[1]] = 2
            queue.append((position[0], position[1], 2))
        for position in arr:
            if new_arr[position[0]][position[1]] == 1:
                new_arr[position[0]][position[1]] = 3
                queue.append((position[0], position[1], 3))
        
        cnt = 0
        while queue:
            size = len(queue)
            memo = []
            for _ in range(size):
                r, c, color = queue.popleft()
                if new_arr[r][c] == 6:
                    continue
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < N and 0 <= nc < M:
                        if new_arr[nr][nc] == 1:
                            new_arr[nr][nc] = color + 2
                            queue.append((nr, nc, color))
                            memo.append((nr, nc, color))
                        elif color == 2 and new_arr[nr][nc] == 5:
                            new_arr[nr][nc] = 6
                            cnt += 1
                        elif color == 3 and new_arr[nr][nc] == 4:
                            new_arr[nr][nc] = 6
                            cnt += 1
            while memo:
                r, c, color = memo.pop()
                if new_arr[r][c] != 6:
                    new_arr[r][c] = color

        answer = max(answer, cnt)               
        return
    
    if idx == len(arr):
        return
    
    selection[sidx] = arr[idx]
    comb(sidx + 1, idx + 1, selection, arr, status)
    comb(sidx, idx + 1, selection, arr, status)


N, M, G, R = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(N)]
start_positions = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(N):
    for c in range(M):
        if garden[r][c] == 2:
            start_positions.append((r, c))

selection = [0] * (G + R)
answer = 0
comb(0, 0, selection, start_positions, 0)
print(answer)