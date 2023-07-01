import sys
from itertools import permutations
input=sys.stdin.readline
N = int(input())
percent_list = list(map(int, input().split()))
answer = 0
flag = False
for i in range(len(percent_list)):
    if percent_list[i] > 50:
        flag = True
        break
    else:
        pass
if flag:
    print(0)
else:
    answer = 0
    permuted_percent_list = list(set(list(permutations(percent_list))))
    for i in permuted_percent_list:
        lines = []
        current = 0
        for num in i:
            current += num
            lines.append(current)
        temp_answer = 0
        for j in range(len(lines)-1):
            for k in range(j+1, len(lines)):
                if lines[j] + 50 == lines[k]:
                    temp_answer += 1
        if answer < temp_answer:
            answer = temp_answer
    print(answer)



