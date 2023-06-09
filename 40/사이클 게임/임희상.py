def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    

N, M = map(int, input().split())

parents = list(range(N))
answer = 0

for i in range(M):
    x, y = map(int, input().split())
    if not answer:
        if find(x) == find(y):
            answer = i+1
    union(x, y)


print(answer)