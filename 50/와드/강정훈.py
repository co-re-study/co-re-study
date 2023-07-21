from collections import deque
import sys
ward_direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
direction = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(R)]
current = list(map(int, sys.stdin.readline().split()))
row_length = len(arr[0])
sight_arr = [["#"]*row_length for _ in range(R)]
current[0], current[1] = current[0] -1, current[1] -1
command = sys.stdin.readline().strip()

for i in range(len(command)):
    current_direction = command[i]
    if current_direction == "W":
        ward_alphabet = arr[current[0]][current[1]]
        queue = deque()
        queue.append((current[0], current[1]))
        visited = set()
        while queue:
            ward_current = queue.popleft()
            sight_arr[ward_current[0]][ward_current[1]] = "."
            if ward_current not in visited:
                visited.add((ward_current[0], ward_current[1]))
                for j in range(4):
                    dr = ward_current[0] + ward_direction[j][0]
                    dc = ward_current[1] + ward_direction[j][1]
                    if (dr < 0 or dc < 0 or dr >= R or dc >= row_length):
                        continue
                    else:
                        if arr[dr][dc] == ward_alphabet and (dr, dc) not in visited:
                            queue.append((dr, dc))
                        else:
                            continue
    else:
        current = (current[0] + direction[current_direction][0], current[1] + direction[current_direction][1])

sight_arr[current[0]][current[1]] = "."
for i in range(4):
    dr = current[0] + ward_direction[i][0]
    dc = current[1] + ward_direction[i][1]
    if dr < 0 or dc < 0 or dr >= R or dc >= row_length:
        continue
    else:
        sight_arr[dr][dc] = "."
for i in sight_arr:
    print("".join(i))