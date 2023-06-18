n, m, k = map(int, input().split())
reqs = []
answer = 0
for _ in range(m):
    reqs.append(list(map(int, input().split())))

def comb(idx, sidx):
    global answer

    if sidx == n:
        skill_set = set(selection)
        counts = 0
        for req in reqs:
            for skill in req:
                if skill not in skill_set:
                    break
            else:
                counts += 1
        answer = max(answer, counts)
        return
    
    if idx == 2*n:
        return
    
    selection[sidx] = skills[idx]
    comb(idx+1, sidx+1)
    comb(idx+1, sidx)

skills = list(range(1, 2*n+1))
selection = [0] * n

comb(0, 0)

print(answer)

