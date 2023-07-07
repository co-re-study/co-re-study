n, k = map(int, input().split())

l = len(str(n))
i = 1
tmp = n

pre = set()
while tmp % k != 0:
    tmp = tmp % k
    if tmp in pre or i >= 1000000000:
        i = -1
        break
    pre.add(tmp)
    i += 1
    tmp = tmp * 10**(l) + n

print(i)
