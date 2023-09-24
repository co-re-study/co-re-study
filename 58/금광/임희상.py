N = int(input())

parents = [0]*2 + list(map(int, input().split()))
children = [[] for _ in range(N+1)]
for i in range(N+1):
    children[parents[i]].append(i)
answer = 0

stack = [(1, 0)]
odds = 0
evens = 0

while stack:
    current, depth = stack.pop()
    if depth % 2:
        odds += 1
    else:
        evens += 1

    for child in children[current]:
        stack.append((child, depth+1))

print(min(odds, evens) + abs(odds-evens))