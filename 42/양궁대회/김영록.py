from itertools import combinations_with_replacement


def solution(n, info):
    answer = []
    ans = 0
    for combi in combinations_with_replacement(range(11), n):
        lion = [0]*11
        for c in combi:
            lion[c] += 1
        peach_score, lion_score = 0, 0
        for i in range(11):
            if not lion[i] and not info[i]:
                continue
            elif info[i] >= lion[i]:
                peach_score += 10-i
            else:
                lion_score += 10-i
        if lion_score - peach_score > ans:
            answer = []
            answer.append(lion)
            ans = lion_score - peach_score
        elif lion_score - peach_score == ans and ans > 0:
            answer.append(lion)
    answer.sort(key=lambda x : x[::-1])    

    return answer[-1] if answer else [-1]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))


'''
어피치 화살 n발 -> 라이언 화살 n발
'''
