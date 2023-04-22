from collections import deque

## 1차시도 (시간초과) 정확성 56.3
def solution(n, roads, sources, destination):
    answer = []
    connection_list = [[] for _ in range(n+1)]
    for road in roads:
        connection_list[road[0]].append(road[1])
        connection_list[road[1]].append(road[0])
    for source in sources:
        dist = 0
        visited = set()
        queue = deque()
        same_dist = deque()
        same_dist.append(source)
        queue.append(source)
        while queue:
            current = queue.popleft()
            same_dist.pop()
            if destination == current:
                answer.append(dist)
                visited.add(current)
                break
            if current in visited:
                continue
            for i in range(len(connection_list[current])):
                location = connection_list[current][i]
                if location not in visited:
                    queue.append(location)
            if not same_dist:
                dist += 1
                same_dist = [i for i in queue]

        if destination not in visited:
            dist = -1
            answer.append(dist)

    return answer

n1 = 5
roads1 = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources1 = 	[1, 3, 5]
destination1 = 5

print(solution(n1, roads1, sources1, destination1))