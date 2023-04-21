n, x, y = map(int,input().split())
numset = set(i for i in range(1, n+1) if i != y-x-1)
myq = []
answer = 0
logger = set()
if x == 1 or y == 1:
    temp = [-1]+[0]*(2*n)
else:
    temp = [0]*(2*n+1)
temp[x] = y-x-1
temp[y] = y-x-1
logger.add(tuple(temp[1:]))
myq.append(temp)
while myq:
    target = myq.pop()
    loopset = numset-set(target)
    if 2*n-target[::-1].index(0)-target.index(0)-1 < max(loopset):
        continue
    for i in loopset:
        lt = target[0]*-1
        while target[lt+1]:
            target[0] -= 1
            lt = target[0]*-1
        tci = target.count(i)
        if target[lt+2+i] or (lt+2+i<=2*n and target[lt+2+i]) or (lt+2+i > 2*n) or tci:
            continue
        temp = target[:]
        temp[0] -= 1
        temp[lt+1] = i
        temp[lt+2+i] = i
        if not temp.count(0):
            if tuple(temp[1:]) not in logger:
                logger.add(tuple(temp[1:]))
                answer += 1
            break
        if tuple(temp[1:]) not in logger:
            logger.add(tuple(temp[1:]))
            myq.append(temp)
print(answer)
