def solution(user_id, banned_id):
    
    # nPr 순열 완탐
    def perm(depth):
        if depth == len(banned_id):
            if tuple(sorted(selection)) in memo:
                return

            visited = [0] * len(banned_id)
            for i in range(len(selection)):
                for j in range(len(banned_id)):
                    if visited[j] or len(banned_id[j]) != len(selection[i]):
                        continue
                    for k in range(len(banned_id[j])):
                        if banned_id[j][k] == "*":
                            continue
                        if banned_id[j][k] != selection[i][k]:
                            break
                    else:
                        visited[j] = 1
                        break
                else:
                    return

            memo.add(tuple(sorted(selection[:])))
            return
        
        for i in range(len(user_id)):
            if not check[i]:
                check[i] = 1
                selection[depth] = user_id[i]
                perm(depth + 1)
                check[i] = 0
        
                        
    selection = [0] * len(banned_id)
    check = [0] * len(user_id)
    memo = set()
    perm(0)

    return len(memo)