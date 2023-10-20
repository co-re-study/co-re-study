import heapq

N = int(input())
people = []
mn = 200000000
mx = 1
for _ in range(N):
    a, b = map(int, input().split())
    x, y = min(a, b), max(a, b)
    people.append((x, y))
    mn = min(mn, x)
    mx = max(mx, y)
D = int(input())

people.sort(key=lambda x: x[1])
answer = 0

# 철로의 길이가 사람들 민맥스보다 크거나 같으면 다 넣을 수 있음
if D >= mx-mn:
    answer = N
else:
    q = []
    for i in range(N):
        home, company = people[i]
        if company - home > D:
            continue
        heapq.heappush(q, (home, company))
        while q[0][0] < company - D:
            heapq.heappop(q)
        answer = max(answer, len(q))

print(answer)