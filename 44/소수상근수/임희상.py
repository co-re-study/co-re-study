n = int(input())

visited = set()
primes = set()

for i in range(2, n+1):
    
    if i in visited:
        continue
    primes.add(i)

    k = i
    while k <= n:
        visited.add(k)
        k += i


def convert(num):

    target = list(map(int, list(str(num))))
    return sum([i * i for i in target])


def determine(num, visited):
    global targets, others

    
    if num in visited:
        others.update(visited)
        return
    visited.add(num)

    converted = convert(num)
    if converted == 1:
        targets.update(visited)
        return
    determine(converted, visited)



targets = set()
others = set()
for num in primes:
    start = num
    if num not in targets or num not in others:
        determine(num, set())

answers = sorted(list(targets&primes))

for answer in answers:
    print(answer)