import sys
input = sys.stdin.readline

N, M = map(int, input().split())
weights = list(map(int, input().split()))
adj_max_weights = [0] * N

for _ in range(M):
    n1, n2 = map(lambda x: int(x) - 1, input().split())
    adj_max_weights[n1] = max(weights[n2], adj_max_weights[n1])
    adj_max_weights[n2] = max(weights[n1], adj_max_weights[n2])

answer = 0
for i in range(N):
    if not adj_max_weights[i] or weights[i] > adj_max_weights[i]:
      answer += 1

print(answer)