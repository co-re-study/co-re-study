import sys
from itertools import combinations
input = sys.stdin.readline

pictures = [tuple(input().split()) for _ in range(9)]
nums = list(range(9))
hap_set = set()

for num_comb in combinations(nums, 3):
    num1, num2, num3 = num_comb
    for i in range(3):
        if pictures[num1][i] != pictures[num2][i] and pictures[num2][i] != pictures[num3][i] and pictures[num3][i] != pictures[num1][i]:
            continue
        if pictures[num1][i] == pictures[num2][i] == pictures[num3][i]:
            continue
        break
    else:
        hap_set.add(num_comb)

n = int(input())
flag = False
answer = 0
for _ in range(n):
    info = input().rstrip()
    if info == "G":
        if not hap_set and not flag:
            answer += 3
            flag = True
        else:
            answer -= 1
    else:
        comb = tuple(sorted(map(lambda x: int(x) - 1, info.split()[1:])))
        if comb in hap_set:
            answer += 1
            hap_set.remove(comb)
        else:
            answer -= 1

print(answer)

