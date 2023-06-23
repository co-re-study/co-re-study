def find(x):
    while x != parents[x]:
        x = parents[x]
    return x


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        if x < y:
            parents[y] = x
        else:
            parents[x] = y


n = int(input())
m = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
tour_lst = [int(x)-1 for x in input().split()]

parents = [i for i in range(n)]

# 연결된 도시들을 루트노드로 묶는다.
for i in range(n):
    for j in range(i+1, n):
        if matrix[i][j] == 1:
            union(i, j)

# 같은 루트 노드를 가지는지 확인한다.
group = find(tour_lst[0])
for city in tour_lst:
    if find(city) != group:
        print("NO")
        break
else:
    print("YES")
