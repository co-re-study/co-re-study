def find(x):
    if root[x] == x:
        return x
    else:
        return find(root[x])


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] > rank[y]:
        root[y] = x

    elif rank[x] < rank[y]:
        root[x] = y
    else:
        root[y] = x
        rank[x] = rank[x]+1


N, M = map(int, input().split())
root = [i for i in range(N)]
rank = [0 for _ in range(N)]
answer = 0
for i in range(M):
    x, y = map(int, input().split())
    if answer == 0:
        if find(x) == find(y):
            answer = i+1
        else:
            union(x, y)

print(answer)
