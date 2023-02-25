# 패션왕 신해빈
for tc in range(int(input())):
    kinds = []
    clothes = []
    for i in range(int(input())):
        cloth, kind = input().split()
        if kind in kinds:
            clothes[kinds.index(kind)].append(cloth)
        else:
            kinds.append(kind)
            clothes.append([cloth])
    answer = 1
    for j in clothes:
        answer *= len(j) + 1

    print(answer - 1)

# from collections import defaultdict

# for tc in range(int(input())):
#     n = int(input())

#     name_dict = defaultdict()
#     clothes = []
#     answer = 0

#     for _ in range(n):
#         name, category = input().split()
#         name_dict[name] = category
#         clothes.append(name)

#     for i in range(1 << n):
#         selected = set()
#         flag = 1
#         for j in range(n):
#             if i & (1 << j):
#                 if name_dict[clothes[j]] in selected:
#                     flag -= 1
#                     break
#                 selected.add(name_dict[clothes[j]])
#         if flag:
#             answer += 1