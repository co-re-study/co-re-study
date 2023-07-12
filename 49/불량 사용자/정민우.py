from itertools import combinations, permutations

def solution(user_id, banned_id):
    answer = 0
    for sub_set in list(combinations(user_id, len(banned_id))):
        for perm_banned_id in list(permutations(banned_id, len(banned_id))):
            count = 0
            for i in range(len(perm_banned_id)):
                if len(sub_set[i]) == len(perm_banned_id[i]):
                    flag = True
                    for j in range(len(sub_set[i])):
                        if perm_banned_id[i][j] != '*' and sub_set[i][j] != perm_banned_id[i][j]:
                            flag = False
                            break
                    if flag:
                        count += 1
            if count == len(perm_banned_id):
                answer += 1
                break
    return answer