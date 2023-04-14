def solution(routes):
    numset = list(set(sum(routes, [])))
    numset.sort()
    numset.append(numset[-1]+1)
    routes.sort(key=lambda x: x[0])
    idx = 0
    visited = set()
    basket = set()
    cnt = 0
    for idx in numset:
        for j in range(len(routes)):
            start, end = routes[j]
            if start <= idx <= end:
                basket.add(j)
            if end < idx:
                if j in basket and j not in visited:
                    visited |= basket
                    cnt += 1
                basket.discard(j)
    return cnt
