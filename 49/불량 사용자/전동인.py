from itertools import permutations


def is_match(user_id, banned_id):
    for i in range(len(user_id)):
        if len(user_id[i]) != len(banned_id[i]):
            return False
        for j in range(len(user_id[i])):
            if banned_id[i][j] == '*':
                continue
            if user_id[i][j] != banned_id[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    arr = list(permutations(user_id, len(banned_id)))
    res = []

    for a in arr:
        if is_match(a, banned_id):
            a = set(a)
            if a not in res:
                res.append(a)
    answer = len(res)
    return answer
