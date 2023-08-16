import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
roads = [list(map(int, input().split())) for _ in range(m)]

adj_list = [[] for _ in range(n + 1)]
parent_cnt = [0] * (n + 1)
for road in roads:
    adj_list[road[0]].append((road[1], road[2]))
    parent_cnt[road[1]] += 1

start, end = map(int, input().split())

# start부터 end까지 DFS
# 각 노드 별로 가장 오랜 시간이 걸렸을 때의 부모 노드 저장
stack = [start]
memo = [0] * (n + 1)
path = [[] for _ in range(n + 1)]
while stack:
    current = stack.pop()
    acc_time = memo[current]
    for destination_info in adj_list[current]:
        destination, cost = destination_info
        if acc_time + cost > memo[destination]:
            memo[destination] = acc_time + cost
            path[destination] = [current]
        elif acc_time + cost == memo[destination]:
            path[destination].append(current)

        # 모든 부모를 다 거친 뒤 자식 노드로 이동
        parent_cnt[destination] -= 1
        if not parent_cnt[destination]:
            stack.append(destination)


print(memo[end])

# end부터 start까지 DFS
# 각 노드 별로 저장해두었던 부모 노드 따라 올라가기
answer = 0
stack = [end]
visited = [0] * (n + 1)
while stack:
    current = stack.pop()
    for destination in path[current]:
        answer += 1
        if not visited[destination]:
            stack.append(destination)
            visited[destination] = 1

print(answer)