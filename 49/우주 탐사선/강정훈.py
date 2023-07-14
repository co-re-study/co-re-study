import sys
input = sys.stdin.readline

def find_answer(current, cost, cnt):
    global answer
    if N == cnt:
        answer = min(answer, cost)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            find_answer(i, cost + graph[current][i], cnt+1)
            visited[i] = 0


N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            graph[j][k] = min(graph[j][i] + graph[i][k], graph[j][k])

# 1차시도 26% 틀
# visited = set()
# visited.add(K)
# current = K
# answer = 0

# while len(visited) < N:
#     answer_candi = 99999999
#     current_candi = 0
#     for i in range(len(graph[current])):
#         if answer_candi > graph[current][i] and i not in visited and current != i:
#             current_candi = i
#             answer_candi = graph[current][i]
#     current = current_candi
#     answer += answer_candi
#     visited.add(current)
# print(answer)

visited = [0]*N
visited[K] = 1
answer = 999999999999
find_answer(K, 0, 1)
print(answer)