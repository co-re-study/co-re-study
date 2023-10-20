n = int(input())
people = []

for _ in range(n):
    h, o = map(int, input().split())
    if h > o:
        h, o = o, h
    people.append((h, o))

d = int(input())
points = []

for i in range(n):
    if people[i][0] + d < people[i][1]:
        continue
    points.append((people[i][0], 1))
    points.append((people[i][1] - d, -1))

points.sort()

counts, answer = 0, 0
for i in range(len(points)):
    counts -= points[i][1]
    answer = max(counts, answer)

print(answer)
