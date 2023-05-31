import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort(reverse=True)

start = 0
end = 2000000000

while start <= end:
    current = (start + end) // 2
    acc = 0
    for tree in trees:
        if tree > current:
            acc += tree - current
    if acc < M:
        end = current - 1
    else:
        start = current + 1

if acc < M:
    current -= 1

print(current)
