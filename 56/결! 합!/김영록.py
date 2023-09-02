from itertools import combinations
images = [0]+[tuple(input().split()) for _ in range(9)]
combi = set()
for x, y, z in combinations(range(1, 10), 3):
    for i in range(3):
        if images[x][i] != images[y][i] and images[y][i] != images[z][i] and images[z][i] != images[x][i]:
            continue
        if images[x][i] == images[y][i] == images[z][i]:
            continue
        break

    else:
        combi.add((x, y, z))
n = int(input())
ans = 0
flag = True
for _ in range(n):
    command = input().split()
    if command[0] == 'H':
        temp = tuple(sorted(map(int, command[1:])))
        if temp in combi:
            combi.discard(temp)
            ans += 1
        else:
            ans -= 1
    else:
        if not combi and flag:
            ans += 3
            flag = False
        else:
            ans -= 1
print(ans)
