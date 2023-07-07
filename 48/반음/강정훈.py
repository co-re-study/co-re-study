## 계음이 고정적이라 지금 푼 링크드리스트 구현으로 푸는 방식은 효율성이 확실히 떨어지는듯

import sys
def ackbo_setting():
    ackbo_dict["A"] = ["GA", "AB"]
    ackbo_dict["AB"] = ["A", "B"]
    ackbo_dict["B"] = ["AB", "C"]
    ackbo_dict["C"] = ["B", "CD"]
    ackbo_dict["CD"] = ["C", "D"]
    ackbo_dict["D"] = ["CD", "DE"]
    ackbo_dict["DE"] = ["D", "E"]
    ackbo_dict["E"] = ["DE", "F"]
    ackbo_dict["F"] = ["E", "FG"]
    ackbo_dict["FG"] = ["F", "G"]
    ackbo_dict["G"] = ["FG", "GA"]
    ackbo_dict["GA"] = ["G", "A"]
input = sys.stdin.readline
ackbo_dict = dict()
ackbo_default_list = ["A", "B", "C", "D", "E", "F", "G"]
N = int(input())
ackbo_list = []
for i in range(N):
    ackbo = int(input())
    ackbo_list.append(ackbo)
answer_list = []
ackbo_setting()
for i in range(len(ackbo_default_list)):
    start_ackbo = ackbo_default_list[i]
    current_ackbo = ackbo_default_list[i]
    flag = True
    for j in range(N):
        standard = ackbo_list[j]
        while standard != 0:
            if standard > 0 :
                current_ackbo = ackbo_dict[current_ackbo][1]
                standard -= 1
            else:
                current_ackbo = ackbo_dict[current_ackbo][0]
                standard += 1
        if len(current_ackbo) == 2:
            flag = False
            break
    if flag:
        answer_list.append([start_ackbo, current_ackbo])

for i in range(len(answer_list)):
    print(*answer_list[i])
