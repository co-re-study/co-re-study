# 왜 첫 번째 코드는 python 시간초과일까요
# 정답을 알려주세요

# pypy 통과, python 시간초과
import sys
from collections import deque
input = sys.stdin.readline

while True:
    N = int(input())
    if not N:
        break

    rooms = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        room_info = input().split()
        rooms[i] = room_info[0], int(room_info[1]), list(map(int, room_info[2:-1]))
    
    if rooms[1][0] == "T" and rooms[1][1] > 0:
        print("No")
        continue

    queue = deque([(1, rooms[1][1])])
    memo = [-1] * (N + 1)
    answer = "No"
    while queue:
        current, acc = queue.popleft()
        if current == N:
            answer = "Yes"
            break
        if acc <= memo[current]:
            continue
        memo[current] = acc

        for adj_node in rooms[current][2]:
            if current == adj_node:
                continue
            if rooms[adj_node][0] == "T":
                if acc - rooms[adj_node][1] > memo[adj_node]:
                    queue.append((adj_node, acc - rooms[adj_node][1]))
            else:
                if max(acc, rooms[adj_node][1]) > memo[adj_node]:
                    queue.append((adj_node, max(acc, rooms[adj_node][1])))

    print(answer)
    
###############################################################
# 둘 다 통과
import sys
from collections import deque
input = sys.stdin.readline

while True:
    N = int(input())
    if not N:
        break

    rooms = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        room_info = input().split()
        rooms[i] = room_info[0], int(room_info[1]), list(map(int, room_info[2:-1]))

    queue = deque([(1, 0)])
    memo = [-1] * (N + 1)
    answer = "No"
    while queue:
        current, acc = queue.pop()

        if memo[current] >= acc:
            continue
        memo[current] = acc

        if rooms[current][0] == "T":
            acc -= rooms[current][1]
        elif rooms[current][0] == "L":
            acc = max(rooms[current][1], acc)
    
        if acc < 0:
            continue

        if current == N:
            answer = "Yes"
            break

        for adj_node in rooms[current][2]:
            queue.append((adj_node, acc))

    print(answer)