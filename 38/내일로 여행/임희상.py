import heapq
def dijkstra(start, end):

    cost_1 = [float('inf')] * len(cities)
    cost_2 = [float('inf')] * len(cities)
    heap = [(0, start)]

    while heap:
        cost, current = heapq.heappop(heap)
        if cost >= cost_1[current]:
            continue
        cost_1[current] = cost
        for destination, next_cost in adj_1[current]:
            if cost_1[destination] > cost_1[current]+next_cost:
                heapq.heappush(heap, (cost_1[current]+next_cost, destination))
    
    heap = [(0, start)]

    while heap:
        cost, current = heapq.heappop(heap)
        if cost >= cost_2[current]:
            continue
        cost_2[current] = cost
        for destination, next_cost in adj_2[current]:
            if cost_2[destination] > cost_2[current]+next_cost:
                heapq.heappush(heap, (cost_2[current]+next_cost, destination))
    
    return cost_1[end], cost_2[end]
    



N, R = map(int, input().split())

cities = list(set(input().split()))
city_dict = {}

adj_1 = [[] for _ in range(len(cities))]
adj_2 = [[] for _ in range(len(cities))]
for i in range(len(cities)):
    city = cities[i]
    if city in city_dict.keys():
        continue
    city_dict[city] = i
    city_dict[i] = city

M = int(input())
target_cities = input().split()

K = int(input())
for _ in range(K):
    train, city1, city2, cost = input().split()
    adj_1[city_dict[city1]].append((city_dict[city2], int(cost)))
    adj_1[city_dict[city2]].append((city_dict[city1], int(cost)))
    if train in {'Mugunghwa', 'ITX-Saemaeul', 'ITX-Cheongchun'}:
        adj_2[city_dict[city1]].append((city_dict[city2], 0))
        adj_2[city_dict[city2]].append((city_dict[city1], 0))
    elif train in {'S-Train', 'V-Train'}:
        adj_2[city_dict[city1]].append((city_dict[city2], int(cost)/2))
        adj_2[city_dict[city2]].append((city_dict[city1], int(cost)/2))
    else:
        adj_2[city_dict[city1]].append((city_dict[city2], int(cost)))
        adj_2[city_dict[city2]].append((city_dict[city1], int(cost)))

total_cost_1 = 0
total_cost_2 = R
for i in range(len(target_cities)-1):
    start, end = city_dict[target_cities[i]], city_dict[target_cities[i+1]]
    choice1, choice2 = dijkstra(start, end)
    total_cost_1 += choice1
    total_cost_2 += choice2
if total_cost_1 > total_cost_2:
    print('Yes')
else:
    print('No')


