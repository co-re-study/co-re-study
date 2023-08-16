import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if not N:
        break

    rooms = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        room_info = input().split()
        rooms[i] = [room_info[0]] + list(map(int, room_info[1:-1]))
    
    if rooms[1][0] == "T" and rooms[1][1] > 0:
        print("No")
        continue

    # DFS
    stack = [(1, rooms[1][1])]
    memo = [-1] * (N + 1)
    answer = "No"
    while stack:
        current, acc = stack.pop()
        if current == N:
            answer = "Yes"
            break
        for adj_node in rooms[current][2:]:
            if current == adj_node:
                continue
            if rooms[adj_node][0] == "T":
                if acc - rooms[adj_node][1] > memo[adj_node]:
                    stack.append((adj_node, acc - rooms[adj_node][1]))
                    memo[adj_node] = acc - rooms[adj_node][1]
            else:
                if max(acc, rooms[adj_node][1]) > memo[adj_node]:
                    stack.append((adj_node, max(acc, rooms[adj_node][1])))
                    memo[adj_node] = max(acc, rooms[adj_node][1])

    print(answer)
    