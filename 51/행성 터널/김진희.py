import heapq
n = int(input())  # 행성 수
arr = [list(map(int, input().split())) for _ in range(n)]

xa = [[] for _ in range(3)]
for i in range(n):
    for j in range(3):
        xa[j].append((arr[i][j], i))
xa[0].sort()
xa[1].sort()
xa[2].sort()

dist = {}
costs = []
heapq.heapify(costs)
for i in range(n - 1):
    for j in range(3):
        if (xa[j][i][1], xa[j][i + 1][1]) in dist.keys():
            dist[(xa[j][i][1], xa[j][i + 1][1])] = min(dist[(xa[j][i][1], xa[j][i + 1][1])],
                                                       xa[j][i+1][0] - xa[j][i][0])
        else:
            dist[(xa[j][i][1], xa[j][i + 1][1])] = xa[j][i + 1][0] - xa[j][i][0]
for d in dist:
    # print(d, dist[d], d[0])
    heapq.heappush(costs, (dist[d], d[0], d[1]))

# print(costs)

parents = list(range(n))


def find_parents(x):
    if parents[x] != x:
        parents[x] = find_parents(parents[x])
    return parents[x]


def union_parents(x, y):
    a, b = find_parents(x), find_parents(y)
    parents[b] = a


answer = 0
while costs:
    cost, r, c = heapq.heappop(costs)
    if find_parents(r) != find_parents(c):
        union_parents(r, c)
        answer += cost

print(answer)