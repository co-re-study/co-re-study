n = int(input())
a = list(map(int, input().split()))
odd = 0
even = 1
parents = list([-1, 0] for _ in range(n + 1))


def find_parent(x):
    global cnt
    if parents[x][0] < 0:
        return x, parents[x][1]
    if parents[x][1] > 0:
        return x, parents[x][1]
    cnt += 1
    parent, acc = find_parent(parents[x][0])
    parents[x] = [parent, acc + cnt]
    return parents[x]


for i in range(n - 1):
    parents[i + 2] = [a[i], 0]

for i in range(2, n + 1):
    cnt = 0
    if find_parent(i)[1] % 2:
        odd += 1
    else:
        even += 1

print(max(odd, even))