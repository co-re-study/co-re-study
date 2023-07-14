from itertools import permutations

N, K = map(int, input().split())
dists = []
for _ in range(N):
    dists.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])

targets = list(range(N))
targets.remove(K)
answer = 1000 * N

for permutation in permutations(targets):
    current = K
    distance = 0
    for destination in permutation:
        distance += dists[current][destination]
        current = destination
    
    answer = min(answer, distance)

print(answer)