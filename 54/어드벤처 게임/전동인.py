from collections import deque


def bfs(graph, n):
    queue = deque()
    queue.append((1, 0))  # 현재 위치, 돈
    visited = set()

    while queue:
        current_room, current_money = queue.popleft()
        room_type, cost, doors = graph[current_room]

        if room_type == 'L':
            current_money = max(current_money, cost)
        elif room_type == 'T':
            if current_money < cost:
                continue
            current_money -= cost

        if current_room == n:
            return True

        for next_room in doors:
            next_state = (next_room, current_money)
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

    return False


while True:
    n = int(input())

    if n == 0:
        break

    graph = {}
    for i in range(1, n+1):
        room_info = input().split()
        room_type = room_info[0]
        cost = int(room_info[1])
        doors = list(map(int, room_info[2:-1]))
        graph[i] = (room_type, cost, doors)

    if bfs(graph, n):
        print("Yes")
    else:
        print("No")
