# cpp, java, python 중 하나
# 백이나 프론트 중 하나를 선택해야함
# junior와 senior 중 하나를 선택
# chicken과 pizza중 하나 선택

# 지원 조건을 선택하면 해당 조건에 맞는 지원자가  몇 명인지 쉽게 알 수 잇는 도구를 만들고 싶음

# java, backend, junior, pizza 선택 중 50점 이상 받은 지원자는?

# 모든 선택을 필수로 할 필요는 없다.

# 4가지 정보, 코딩테스트 점수 하나의 문자열로 구성한 값의 배열 info
# 개발팀이 궁금해하는 문의 조건이 문자열 형태로 담긴 배열query가 매개변수
# 각 문의 조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return

# 딕셔너리에 lan, pos, prof, food, score
# 셋으로 교집합으로 해서

# def solution(info, query):
#     answer = []
#     entire = defaultdict(dict)
#     entire['lan'] = defaultdict(set)
#     entire['pos'] = defaultdict(set)
#     entire['prof'] = defaultdict(set)
#     entire['food'] = defaultdict(set)
#     entire['score']= defaultdict(int)
#
#     #딕셔너리에 넣기
#     for i1 in range(len(info)):
#         tmp1 = list(info[i1].split(' '))
#         entire['lan'][tmp1[0]].add(i1)
#         entire['pos'][tmp1[1]].add(i1)
#         entire['prof'][tmp1[2]].add(i1)
#         entire['food'][tmp1[3]].add(i1)
#         entire['score'][i1] = tmp1[4]
#     entire['lan']['-'] = entire['lan']['cpp'] | entire['lan']['java'] | entire['lan']['python']
#     entire['pos']['-'] = entire['pos']['backend'] | entire['pos']['frontend']
#     entire['prof']['-'] = entire['prof']['junior'] | entire['prof']['senior']
#     entire['food']['-'] = entire['food']['chicken'] | entire['food']['pizza']
#
#     #쿼리 정보검색
#     for i2 in range(len(query)):
#         #조건 검색
#         tmp2 = list(query[i2].split(' and '))
#         tmp3 = list(tmp2[3].split(' ')) #첫번째는 음식 두번째는 점수
#
#         #언어 검색
#         if tmp2[0] == "-":
#             first = entire['lan']['-']
#         else:
#             first = entire['lan'][tmp2[0]]
#         if tmp2[1] == '-':
#             scnd = entire['pos']['-']
#         else:
#             scnd = entire['pos'][tmp2[1]]
#         if tmp2[2] == '-':
#             thrd = entire['prof']['-']
#         else:
#             thrd = entire['prof'][tmp2[2]]
#         #음식
#         if tmp3[0] == '-':
#             frth = entire['food']['-']
#         else:
#             frth = entire['food'][tmp3[0]]
#         #합산 하기
#         condition = first & scnd & thrd & frth
#         cal = 0
#         for i3 in (condition):
#             if int(entire['score'][i3]) >= int(tmp3[1]):
#                 cal += 1
#         answer.append(cal)
#
#     return answer

from collections import *
from itertools import combinations
def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    #정보 넣기
    for i1 in info:
        tmp = list(i1.split(' '))
        except_value = tmp[:-1]
        value = int(tmp[-1])
        for i2 in range(5):
            for i3 in combinations(except_value,i2):
                tmp_key = ''.join(i3)
                info_dict[tmp_key].append(value)
    for v in info_dict:
        info_dict[v].sort()

    for j1 in query:
        tmp2 = j1.split(' and ')
        while '-' in tmp2:
            tmp2.remove('-')
        query_tmp = tmp2[-1].split(' ')
        val_query = int(query_tmp[1])
        if query_tmp[0] != "-":
            tmp2 = ''.join(tmp2[:-1]) + query_tmp[0]
        else:
            tmp2 = ''.join(tmp2[:-1])

        if tmp2 in info_dict:
            score = info_dict[tmp2]
            if score:
                answer.append(binary_search(val_query,score))
        else:
            answer.append(0)
    return answer


def binary_search(t,lst):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (end +  start)//2
        if lst[mid] >= t:
            end = mid - 1
        else:
            start = mid + 1
    return len(lst) - end - 1

        # 맨 처음이거나
        # 맨 마지막이거나
        # 왼쪽은 작고 오른쪽은 크고

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))

