def solution(routes):
    answer = 0
    routes.sort(key=lambda x:[x[1], x[0]])
    k = 0
    index = 0
    while k < len(routes):
        index = routes[k][1]
        for i in range(k, len(routes)):
            if routes[k][0] <= index <= routes[k][1]:
                k += 1
            else:
                break
        answer += 1

    return answer


routes1 = [[-20,-15], [-20,-16], [-17,-13], [-13,10]]
print(solution(routes1))
