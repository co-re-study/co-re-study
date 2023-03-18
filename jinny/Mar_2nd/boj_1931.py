#회의실배정
n = int(input())
q = []
for _ in range(n):
    s, e = map(int, input().split())
    q.append((e, s))
q.sort(key=lambda x: (x[0], x[1]))

answer = 0
now = (0, 0)
for i in range(n):
    if q[i][1] >= now[0]:
        answer += 1
        now = q[i]
print(answer)
