import sys
from copy import deepcopy
input = sys.stdin.readline

D = int(input())
N = 8
adj_list = [
    [1, 2],        # 정보과학관
    [0, 2, 3],     # 전산관
    [0, 1, 3, 4],  # 미래관
    [1, 2, 4, 5],  # 신양관
    [2, 3, 5, 6],  # 한경직기념관
    [3, 4, 7],     # 진리관
    [4, 7],        # 형남공학관
    [5, 6]         # 학생회관
]

dp = [[[0] * N for _ in range(N)] for _ in range(30)]
for i in range(N):
    for dest in adj_list[i]:
        dp[0][i][dest] = 1

for i in range(29):
    for j in range(N):
        for k in range(N):
            for p in range(N):
                dp[i + 1][j][p] = (dp[i + 1][j][p] + dp[i][j][k] * dp[i][k][p]) % 1000000007

power = 29
cnt_dict = {0: 1}
while power >= 0:
    if D >= 1 << power:
        new_dict = dict()
        for current in cnt_dict:
            for dest in range(N):
                if dp[power][current][dest]:
                    if dest in new_dict:
                        new_dict[dest] = (new_dict[dest] + cnt_dict[current] * dp[power][current][dest]) % 1000000007
                    else:
                        new_dict[dest] = (cnt_dict[current] * dp[power][current][dest]) % 1000000007
        cnt_dict = deepcopy(new_dict)
        D -= 1 << power
    power -= 1

if 0 not in cnt_dict:
    print(0)
else:
    print(cnt_dict[0])