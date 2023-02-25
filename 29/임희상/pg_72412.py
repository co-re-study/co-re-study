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

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])