def calc_stat(team):
    sum_stat = 0
    for member in team:
        for other_member in team:
            if member != other_member:
                sum_stat += S[member][other_member]
    return sum_stat

N = int(input())
S, ans, member_set, member_list = [list(map(int, input().split())) for _ in range(N)], 9999999999999999999, set(range(N)), list(range(N))

for i in range(1 << N):
    team_start = set()
    for j in range(N):
        if i & (1 << j):
            team_start.add(member_list[j])
    if team_start and len(team_start) < N:
        stat_diff = abs(calc_stat(team_start) - calc_stat(member_set - team_start))
        if stat_diff < ans:
            ans = stat_diff
print(ans)
