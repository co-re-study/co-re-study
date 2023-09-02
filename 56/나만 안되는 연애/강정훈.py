import heapq


def find_root(x):
    if x != root[x]:
        root[x] = find_root(root[x])
    return root[x]


def union(x, y):
    x = find_root(x)
    y = find_root(y)
    if rank[x] > rank[y]:
        root[y] = root[x]
    elif rank[y] > rank[x]:
        root[x] = root[y]
    else:
        root[x] = root[y]
        rank[x] += 1


N, M = map(int, input().split())
gender_list = ["0"] + input().split()
root = [i for i in range(N+1)]
rank = [0 for _ in range(N+1)]
edges = []

for i in range(M):
    start, end, dist = map(int, input().split())
    edges.append((dist, start, end))
result = 0
heapq.heapify(edges)
while edges:
    dist, start, end = heapq.heappop(edges)
    if (find_root(start) != find_root(end)) and gender_list[start] != gender_list[end]:
        union(start, end)
        result += dist

final_root = 0
flag = True
for i in range(1, N+1):
    if i == 1:
        final_root = find_root(i)
    else:
        if final_root != find_root(i):
            flag = False
            break
if flag:
    print(result)
else:
    print(-1)

