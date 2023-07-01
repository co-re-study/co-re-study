import itertools

n = int(input())
percents = sorted(list(map(int, input().split())))
per = itertools.permutations(percents, n)

ans = 0
for p in per:
    crr = 0

    # 누적합
    haps = []
    sum = 0
    for e in p:
        sum += e
        haps.append(sum)

    # 차가 50인 경우를 완탐
    size = len(haps)
    for i in range(size-1):
        for j in range(i+1, size):
            if haps[j]-haps[i] == 50:
                crr += 1

    if crr > ans:
        ans = crr

print(ans)
