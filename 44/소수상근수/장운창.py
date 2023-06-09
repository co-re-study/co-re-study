N = int(input())
numc = [0 for _ in range(N+1)]
primes = set()
# 소수판별
numc[0] = 1
numc[1] = 1
for i in range(N+1):
    if numc[i] == 1:
        continue
    else:
        for j in range(i*2, N+1, i):
            numc[j] = 1
for target in (x for x in range(N+1) if not numc[x]):
    # 상근수 판별
    mem = {target}
    worked = False
    nontarget = target
    while nontarget != 1:
        temp = 0
        for w in str(nontarget):
            temp += int(w)**2
        nontarget = temp
        if temp in mem:
            worked = True
            break
        mem.add(temp)
    if not worked:
        primes.add(target)
print(*sorted(list(primes)),sep='\n')
