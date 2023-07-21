## 1차시도 시간 초과... 1%밖에 뚫지 못했다..
# from itertools import combinations
# import sys
# input=sys.stdin.readline
# MBTI_list = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
# MBTI_counting_dict = dict()
#
# MBTI_dict = dict()
# def make_MBTI_dict():
#     for i in range(len(MBTI_list)):
#         for j in range(i, len(MBTI_list)):
#             cnt = 0
#             for k in range(4):
#                 if MBTI_list[i][k] != MBTI_list[j][k]:
#                     cnt += 1
#             MBTI_dict[(MBTI_list[i], MBTI_list[j])] = cnt
#             MBTI_dict[(MBTI_list[j], MBTI_list[i])] = cnt
# make_MBTI_dict()
# T = int(input())
# for i in range(T):
#     N = int(input())
#     combi_list = list(combinations(list(input().split()), 3))
#     psychological_dist = 99999999999999
#     for three_people in combi_list:
#         three_people_combi = list(combinations(three_people, 2))
#         min_dist_candi = 0
#         for key in three_people_combi:
#             min_dist_candi += MBTI_dict[key]
#         if psychological_dist > min_dist_candi:
#             psychological_dist = min_dist_candi
#         if psychological_dist == 0:
#             break
#     print(psychological_dist)


## 2차 시도 너무 화남
# MBTI_dict = dict()
# T = int(input())
# for i in range(T):
#     N = int(input())
#     combi_list = list(set(combinations(list(input().split()), 3)))
#     psychological_dist = 99999999999999
#     for three_people in combi_list:
#         three_people_combi = list(combinations(three_people, 2))
#         min_dist_candi = 0
#         for key in three_people_combi:
#             if key not in MBTI_dict:
#                 cnt = 0
#                 for j in range(4):
#                     if key[0][j] != key[1][j]:
#                         cnt += 1
#                 MBTI_dict[key] = cnt
#                 MBTI_dict[(key[1], key[0])] = cnt
#                 min_dist_candi += cnt
#             else:
#                 min_dist_candi += MBTI_dict[key]
#         if psychological_dist > min_dist_candi:
#             psychological_dist = min_dist_candi
#         if psychological_dist == 0:
#             break
#     print(psychological_dist)

### 3차 시도 비둘기집 원리를 파악하고 적용해보려고 시도. 성공

import sys
from itertools import combinations
input=sys.stdin.readline
MBTI_list = ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
MBTI_dict = dict()
T = int(input())
for i in range(T):
    MBTI_counting_dict = dict()
    N = int(input())
    MBTI_input_list = list(input().split())
    flag = False
    '''
    비둘기집 원리 적용
    시간 초과가 나는 경우는 N의 범위가 커질 때 발생한다.
    같은 MBTI 유형의 사람이 세 사람이 있다면 결국, 세 사람의 심리적 거리 최소는 0이다.
    16가지로 MBTI의 종류가 한정된 상황에서, N의 크기가 커질 수록 MBTI 유형이 겹칠 수 밖에 없다.(N이 257(16^^2+1)이상부터는 
    한 가지 MBTI 유형이 3명 이상 무조건 겹치는 상황이 나온다.
    '''
    for j in MBTI_input_list:
        if j not in MBTI_counting_dict:
            MBTI_counting_dict[j] = 1
        else:
            MBTI_counting_dict[j] += 1
        if MBTI_counting_dict[j] == 3:
            flag = True
            break
    if flag:
        print(0)

    # 한 가지 MBTI가 3개 이상 안 겹친다면 N의 값이 작기 때문에, 부담 없이 돌려도 된다.
    else:
        combi_list = list(set(combinations(MBTI_input_list, 3)))
        psychological_dist = 99999999999999
        for three_people in combi_list:
            three_people_combi = list(combinations(three_people, 2))
            min_dist_candi = 0
            for key in three_people_combi:
                if key not in MBTI_dict:
                    cnt = 0
                    for j in range(4):
                        if key[0][j] != key[1][j]:
                            cnt += 1
                    MBTI_dict[key] = cnt
                    MBTI_dict[(key[1], key[0])] = cnt
                    min_dist_candi += cnt
                else:
                    min_dist_candi += MBTI_dict[key]
            if psychological_dist > min_dist_candi:
                psychological_dist = min_dist_candi
        print(psychological_dist)

