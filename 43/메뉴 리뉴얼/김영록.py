'''
각 손님 단품메뉴 2개 이상
가장 많이 주문
최소 2명 이상
'''
from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    for i in course:
        ans = Counter()
        for order in orders:
            order= sorted(list(order))
            ans += Counter(combinations(order, i))
        answer += [''.join(key) for key, value in ans.most_common()
                   if value == ans.most_common()[0][1] and value > 1]
        answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
