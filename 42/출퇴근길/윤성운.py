import sys

def dfs(start, end, adj_list):
    stack = [start]
    visited = set()
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        for destination in adj_list[current]:
            if destination != end and destination not in visited:
                stack.append(destination)
    return visited


n, m = map(int, input().split())
adj_list = [[] for _ in range(n + 1)]
adj_rev_list = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_rev_list[end].append(start)

start, end = map(int, input().split())

# 출발 정방향
start_forward = dfs(start, end, adj_list)

# 출발 역방향
start_reverse = dfs(end, -1, adj_rev_list)

# 출발 경로 저장
start_path = set()
for node in start_forward:
    if node in start_reverse:
        start_path.add(node)

# 도착 정방향
end_forward = dfs(end, start, adj_list)

# 도착 역방향
end_reverse = dfs(start, -1, adj_rev_list)

# 도착 경로 저장
end_path = set()
for node in end_forward:
    if node in end_reverse:
        end_path.add(node)

# 겹치는 경로 카운트
answer = 0
for node in start_path:
    if node in end_path:
        answer += 1

print(answer)