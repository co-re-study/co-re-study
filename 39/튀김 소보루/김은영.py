n, s = map(int, input().split())
m = int(input())

bread = [0]
for i in range(m):
    bread.append(int(input()))

x, t, r = 0, 0, 0
while x != (n-s):
    for i in range(1, m+1):
        if t % bread[i] == 0:
            x += 1
            r = i
            if x == (n - s):
                break
    t += 1


print(r)

