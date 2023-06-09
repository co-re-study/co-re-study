# 우선 자식 부모 간에서 부모가 얼리어답터면 되는거 같은데..
# tree dp 몰라아아아아 할 줄 모른다고오오오오오오오오옹
# 메모리초과라니ㅣ이이이이이이이이이이 쥐에에에에ㅔㄴ장아아아아앙

def find_parent(prev, depth):
    global ans
    if prev != 1:
        ans.add(prev)
        if parent[child[prev]]:
            for jdx in parent[child[prev]]:
                ans.add(jdx)
    if depth == n:
        return
    else:
        for idx in range(1, n+1):
            if tree[depth][idx]:
                find_parent(depth, idx)
        return


n = int(input())
tree = [[0] * (n+1) for _ in range(n+1)]
parent = dict()
child = dict()
while True:
    a, b = map(int, input().split(" "))
    if a not in parent:
        parent[a] = []
    parent[a].append(b)
    child[b] = a
    tree[a][b] = 1
    if b == n:
        break

ans = set()
find_parent(1, 1)
print(len(ans))