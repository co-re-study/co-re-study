from itertools import combinations
from collections import defaultdict


def solution(info, query):
    answer = []
    infos = defaultdict(list)
    for i in info:
        i = i.split()
        for j in range(5):
            for c in combinations(i[:-1], j):
                infos[''.join(c)].append(int(i[-1]))
    for k in infos.keys():
        infos[k].sort()
    for q in query:
        q = q.replace('and', '').replace('-', '').split()
        target = infos[''.join(q[:-1])]
        s, e = 0, len(target)
        while s < e:
            m = (s+e)//2
            if target[m] < int(q[-1]):
                s = m+1
            else:
                e = m
        answer.append(len(target)-s)
    return answer


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
      "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
