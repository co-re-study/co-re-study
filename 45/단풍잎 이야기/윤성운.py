import sys
input = sys.stdin.readline

def comb(sidx, idx):
    global answer

    if sidx == n:
        selection_set = set(selection)
        cnt = 0
        for quest in quests:
            for num in quest:
                if num not in selection_set:
                    break
            else:
                cnt += 1
        if cnt > answer:
            answer = cnt
        return
    
    if idx == 2 * n:
        return
    
    selection[sidx] = nums[idx]
    comb(sidx + 1, idx + 1)
    comb(sidx, idx + 1)
    

n, m, k = map(int, input().split())
quests = [list(map(int, input().split())) for _ in range(m)]

nums = list(range(1, 2 * n + 1))
selection = [0] * n
answer = 0

comb(0, 0)
print(answer)
