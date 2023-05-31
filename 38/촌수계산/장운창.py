N = int(input())
X, Y = map(int,input().split())
M = int(input())
family = [[] for x in range(N+1)]
for i in range(M):
    x, y = map(int,input().split())
    family[x].append(y)
    family[y].append(x)
val = -1
def dfs(n, cnt, visited):
    for i in family[n]:
        if i not in visited:
            if i == Y:
                global val
                val = cnt+1
            dfs(i, cnt+1, visited+[i])
dfs(X, 0, [X])
print(val)
