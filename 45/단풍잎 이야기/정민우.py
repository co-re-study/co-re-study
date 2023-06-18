n, m, k = map(int, input().split())
quest_list = []
skill_set = set()
for _ in range(m):
    now_quest = set(map(int, input().split()))
    quest_list.append(now_quest)
    skill_set = skill_set | now_quest

skill_list = list(skill_set)
ans = 0
s = len(skill_list)

for i in range(1 << s):
    skill_subset = set()
    for j in range(s):
        if i & (1 << j):
            skill_subset.add(skill_list[j])
    if len(skill_subset) <= n:
        count = 0
        for quest in quest_list:
            if len(skill_subset & quest) == k:
                count += 1
        if count > ans:
            ans = count

print(ans)