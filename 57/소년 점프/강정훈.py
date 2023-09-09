from collections import deque
import sys
input=sys.stdin.readline

R, C = map(int, input().split())
arr = [input() for _ in range(R)]
billian_time = [[0 for _ in range(C)] for _ in range(R)]
billian_start_list = []
for i in range(3):
    x, y = map(int, input().split())
    billian_start_list.append((x-1, y-1, 0, i))

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited_dict = {0: set(), 1: set(), 2: set()}
for start in billian_start_list:
    q = deque([start])
    visited_dict[start[3]].add((start[0], start[1]))
    while q:
        current = q.popleft()
        for dx, dy in direction:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < R and 0 <= y < C:
                if arr[x][y] == '0' and (x, y) not in visited_dict[current[3]]:
                    visited_dict[current[3]].add((x, y))
                    billian_time[x][y] = max(billian_time[x][y], current[2]+1)
                    q.append((x, y, current[2]+1, current[3]))
min_value = 9999999999
cnt = 1
for i in range(R):
    for j in range(C):
        if (i, j) in visited_dict[0] and (i, j) in visited_dict[1] and (i, j) in visited_dict[2]:
            if min_value > billian_time[i][j]:
                min_value = billian_time[i][j]
                cnt = 1
            elif min_value == billian_time[i][j]:
                cnt += 1
if min_value == 9999999999:
    print(-1)
else:
    print(min_value)
    print(cnt)


