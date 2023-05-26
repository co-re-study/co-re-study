N, C = map(int, input().split())
homes = []
for _ in range(N):
    homes.append(int(input()))

homes.sort()


def determine(length):
    current = homes[0]
    dist = 0
    machine = C - 1
    for home in homes:
        if home == homes[0]:
            continue
        dist += home - current
        if dist >= length:
            machine -= 1
            dist = 0
            if not machine:
                return True
        current = home
    return False


left = 0
right = 1000000001
prev = 0

while left < right:
    mid = (right + left) // 2
    if determine(mid):
        left = mid
    else:
        right = mid
    if mid == prev:
        break
    prev = mid

print(mid)