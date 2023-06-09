from collections import deque

# 아이디어: 특정 리프에서 시작하여 가장 먼 리프들을 탐색한다. 가장 먼 리프가 최대값이고, 두 번째로 먼 리프가 중간값이다.
# 아무 노드나 집어서 리프를 탐색한다.
# 리프를 찾는 가장 간단한 방법은 아무 노드를 집어서 depth가 가장 깊은 노드를 탐색하여 아무거나 집으면 확실하게 리프다.
def solution(n, edges):
    answer = 0
    trees = [[] for _ in range(n + 1)]

    # 트리 만들기
    for i in range(len(edges)):
        trees[edges[i][0]].append(edges[i][1])
        trees[edges[i][1]].append(edges[i][0])
    # 1에서 시작하여 아무 리프나 찾을 예정
    queue = deque()
    queue.append((1, 0))
    first_visited = set()
    distance = []
    # 리프를 찾아야함.
    while queue:
        current, depth = queue.popleft()
        distance.append((current, depth))
        first_visited.add(current)
        for i in trees[current]:
            if i not in first_visited:
                queue.append((i, depth + 1))
    leaf = distance[-1][0]
    queue.append((leaf, 0))
    second_visited = set()
    while queue:
        current, depth = queue.popleft()
        distance.append((current, depth))
        second_visited.add(current)
        for i in trees[current]:
            if i not in second_visited:
                queue.append((i, depth + 1))

    if distance[-1][1] == distance[-2][1]:
        answer = distance[-1][1]
        return answer

    third_visited = set()
    queue.append((distance[-1][0], 0))
    while queue:
        current, depth = queue.popleft()
        distance.append((current, depth))
        third_visited.add(current)
        for i in trees[current]:
            if i not in third_visited:
                queue.append((i, depth + 1))
    return distance[-2][1]

n1 = 4
edges1 = [[1,2],[2,3],[3,4]]
n2 = 5
edges2 = [[1,5],[2,5],[3,5],[4,5]]

print(solution(n1, edges1))
print(solution(n2, edges2))