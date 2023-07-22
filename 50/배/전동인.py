n = int(input())
f_days = [int(input()) for _ in range(n)]

loops = []

for i in range(1, n):
    loop = f_days[i] - 1
    if not loops:
        loops.append(loop)

    flag = True
    for l in loops:
        if loop % l == 0:
            flag = False
            pass
    else:
        if flag:
            loops.append(loop)

print(len(loops))
