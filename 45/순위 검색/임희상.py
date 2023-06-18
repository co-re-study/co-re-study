from itertools import combinations
def solution(info, query):
    answer = []
    languages = {'cpp', 'java', 'python'}
    positions = {'backend', 'frontend'}
    careers = {'junior', 'senior'}
    soulfoods = {'pizza', 'chicken'}
    properties_combinations = {}
    properties_combinations[()] = []
    for language in languages:
        for position in positions:
            for career in careers:
                for soulfood in soulfoods:
                    for n in range(1, 5):
                        for combination in combinations([language, position, career, soulfood], n):
                            properties_combinations[combination] = []

    for person in info:
        person = person.split()
        properties_combinations[()].append(int(person[-1]))
        for n in range(1, 5):
            for target in combinations(person[:-1], n):
                properties_combinations[target].append(int(person[-1]))
    for combination in properties_combinations:
        properties_combinations[combination].sort()

    for conditions in query:
        conditions = conditions.split()
        cut_off = int(conditions[-1])
        target = []
        for condition in conditions:
            if condition == 'and':
                continue
            if condition != '-':
                target.append(condition)
        candidates = properties_combinations[tuple(target[:-1])]
        left = 0
        right = len(candidates) - 1
        answer.append(0)
        while 0 <= left <= right <= len(candidates)-1:
            mid = (right+left)//2
            if candidates[mid] < cut_off:
                left = mid + 1
                answer[-1] = len(candidates) - 1 - mid
            else:
                right = mid
                if left == right:
                    answer[-1] = len(candidates) - mid
                    break

    return answer