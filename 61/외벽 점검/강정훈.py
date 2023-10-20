def solution(n, weak, dist):

    repair_list = [()]
    answer = 0
    dist.sort(reverse=True)

    for move_dist in dist:
        new_repairs = []
        answer += 1

        # 수리 가능한 지점 찾기
        for i in range(len(weak)):
            start = weak[i]
            ends = weak[i:] + [n+w for w in weak[:i]]
            can_weak_points = []
            for end in ends:
                if end - start <= move_dist:
                    can_weak_points.append(end % n)
            new_repairs.append(set(can_weak_points))

        candi = set()
        for new_repair_set in new_repairs:
            for repair_set in repair_list:
                new_repair = new_repair_set | set(repair_set)
                if len(new_repair) == len(weak):
                    return answer
                candi.add(tuple(new_repair))
        repair_list = candi

    return -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))