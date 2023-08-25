import sys
input=sys.stdin.readline
N, Q = map(int, input().split())
team_list = [0] + list(map(int, input().split()))
accumulated_popular = [0]
accumulated_fun_list = [0]
for i in range(1, len(team_list)):
    accumulated_popular.append(team_list[i] + accumulated_popular[i-1])
    accumulated_fun_list.append(accumulated_fun_list[i-1] + accumulated_popular[i-1]*team_list[i])
divisions = [list(map(int, input().split())) for _ in range(Q)]
for l, r in divisions:
    answer = (accumulated_fun_list[r] - (accumulated_fun_list[l-1] + (accumulated_popular[r] - accumulated_popular[l-1])*accumulated_popular[l-1]))
    print(answer)

# 식은 간단하지만, 위 식을 도출하는데 너무 머리아프고 오래걸림..