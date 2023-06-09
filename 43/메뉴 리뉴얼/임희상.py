from itertools import combinations
def solution(orders, course):
    answer = []
    for num in course:
        menus = {}
        counts = [set() for _ in range(21)]
        for order in orders:
            order = list(order)
            combination = list(combinations(order, num))
            for target in combination:
                target = ''.join(sorted(list(target)))
                if target in menus.keys():
                    counts[menus[target]].discard(target)
                    menus[target] += 1
                    counts[menus[target]].add(target)
                else:
                    menus[target] = 1
                    counts[1].add(target)
        for i in range(20, 1, -1):
            if counts[i]:
                answer.extend(counts[i])
                break
    answer.sort()

    return answer