import sys
input = sys.stdin.readline

N = int(input())

adj = [{} for _ in range(N+1)]

for _ in range(N-1):
    start, end, dist = map(int, input().split())
    adj[start][end] = dist
    adj[end][start] = dist

ancestors = [[[0, 0, 0] for _ in range(20)] for _ in range(N+1)]
stack = [(1, 0)]
levels = [0] * (N+1)
visited = set()

while stack:
    current, level = stack.pop()
    visited.add(current)
    levels[current] = level
    for destination in adj[current].keys():
        if destination not in visited:
            ancestors[destination][0] = [current, adj[current][destination], adj[current][destination]]
            stack.append((destination, level+1))
    
    temp = 1
    level //= 2
    while level:
        ancestors[current][temp] = [ancestors[ancestors[current][temp-1][0]][temp-1][0], 
                                              min(ancestors[current][temp-1][1], ancestors[ancestors[current][temp-1][0]][temp-1][1]),
                                              max(ancestors[current][temp-1][2], ancestors[ancestors[current][temp-1][0]][temp-1][2])]
        level //= 2
        temp += 1


for _ in range(int(input())):
    start, end = map(int, input().split())

    power = 18
    target = start if levels[start] > levels[end] else end
    other = end if levels[start] > levels[end] else start
    diff = abs(levels[target] - levels[other])
    min_dist = float("INF")
    max_dist = 0

    for i in range(19, -1, -1):
        if 2**i <= diff:
            min_dist = min(min_dist, ancestors[target][i][1])
            max_dist = max(max_dist, ancestors[target][i][2])
            target = ancestors[target][i][0]
            diff -= 2**i

    if target == other:
        print(min_dist, max_dist)
        continue

    for i in range(19, -1, -1):
        if ancestors[target][i][0] != ancestors[other][i][0]:
            min_dist = min(min_dist, ancestors[target][i][1], ancestors[other][i][1])
            max_dist = max(max_dist, ancestors[target][i][2], ancestors[other][i][2])
            target = ancestors[target][i][0]
            other = ancestors[other][i][0]
    
    min_dist = min(min_dist, ancestors[target][i][1], ancestors[other][i][1])
    max_dist = max(max_dist, ancestors[target][i][2], ancestors[other][i][2])
    
    print(min_dist, max_dist)
            
