import heapq


def find(x):
    while x != parents[x]:
        x = parents[x]
    return x


def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        x, y = y, x
    parents[y] = x


n = int(input())
planets = [list(map(int, input().split())) + [i]
           for i in range(n)]  # 행성 번호 추가 저장
parents = [i for i in range(n)]

# 가까운 행성끼리만 cost 계산
edges = []
for i in range(3):
    planets.sort(key=lambda x: x[i])  # 각 좌표별로 정렬
    for j in range(1, n):
        edges.append((abs(planets[j-1][i] - planets[j][i]),
                     planets[j-1][3], planets[j][3]))  # 비용, 시작행성, 끝행성

heapq.heapify(edges)

# 사이클이 형성되지 않게 연결, 간선수 : N-1
result = 0
while edges:
    cost, x, y = heapq.heappop(edges)
    if find(x) != find(y):
        union(x, y)
        result += cost

print(result)
