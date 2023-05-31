import sys
input = sys.stdin.readline

N, R = map(int, input().split())
cities = list(set(input().split()))
idx_dict = dict()
for i in range(len(cities)):
    idx_dict[cities[i]] = i
M = int(input())
destinations = input().split()
K = int(input())
INF = 987654321

# 0번째: 내일로 아닌 버전, 1번째: 내일로 버전
distances = [[[INF, INF] for _ in range(len(cities))] for _ in range(len(cities))]
for i in range(len(cities)):
    for j in range(len(cities)):
        if i == j:
            distances[i][j] = [0, 0]

for _ in range(K):
    transportation, city1, city2, cost = input().split()
    cost = int(cost)
    naeilro_cost = cost
    if transportation in {"Mugunghwa", "ITX-Saemaeul", "ITX-Cheongchun"}:
        naeilro_cost = 0
    elif transportation in {"S-Train", "V-Train"}:
        naeilro_cost /= 2

    if cost < distances[idx_dict[city1]][idx_dict[city2]][0]:
        distances[idx_dict[city1]][idx_dict[city2]][0] = cost
        distances[idx_dict[city2]][idx_dict[city1]][0] = cost
    if naeilro_cost < distances[idx_dict[city1]][idx_dict[city2]][1]:
        distances[idx_dict[city1]][idx_dict[city2]][1] = naeilro_cost
        distances[idx_dict[city2]][idx_dict[city1]][1] = naeilro_cost

# 플로이드 와샬
for i in range(len(cities)):
    for j in range(len(cities)):
        for k in range(len(cities)):
            if distances[j][i][0] + distances[i][k][0] < distances[j][k][0]:
                distances[j][k][0] = distances[j][i][0] + distances[i][k][0]
                distances[k][j][0] = distances[j][i][0] + distances[i][k][0]
            if distances[j][i][1] + distances[i][k][1] < distances[j][k][1]:
                distances[j][k][1] = distances[j][i][1] + distances[i][k][1]
                distances[k][j][1] = distances[j][i][1] + distances[i][k][1]

total_cost = 0
total_naeilro_cost = R
for i in range(len(destinations) - 1):
    start, end = destinations[i], destinations[i + 1]
    total_cost += distances[idx_dict[start]][idx_dict[end]][0]
    total_naeilro_cost += distances[idx_dict[start]][idx_dict[end]][1]

if total_naeilro_cost < total_cost:
    print("Yes")
else:
    print("No")