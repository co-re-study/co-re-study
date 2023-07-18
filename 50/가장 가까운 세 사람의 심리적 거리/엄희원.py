from itertools import combinations_with_replacement as c

from copy import deepcopy

T = int(input())

mbtis = ['ESTP', 'ESTJ', 'ESFP', 'ESFJ', 'ENFP', 'ENFJ', 'ENTP', 'ENTJ',
        'ISTP', 'ISTJ', 'ISFP', 'ISFJ', 'INFP', 'INFJ', 'INTP', 'INTJ']

mbti_comb = list(c(mbtis, 3))

mbti_dict = {}

for m in mbti_comb:
    dist = 0
    j = 0
    for k in range(4):
        if m[j][k] != m[j+1][k]:
            dist += 1
        if m[j][k] != m[j+2][k]:
            dist += 1
    j = 1
    for k in range(4):
        if m[j][k] != m[j+1][k]:
            dist += 1

    if dist in mbti_dict:
        mbti_dict[dist].append(m)
    else:
        mbti_dict[dist] = [m]

for tc in range(T):
    N = int(input())

    m = list(input().split())
    ans = 0
    flag = True
    for i in range(0,9,2):
        if flag == False:
            break
        for mbs in mbti_dict[i]: # ('ESTP', 'ESTP', 'ESTP')
            if flag == False:
                break
            mbs_copy = list(deepcopy(mbs))
            for mb in m:
                if flag == False:
                    break
                for j in range(len(mbs_copy)):
                    if mbs_copy[j] == mb:
                        mbs_copy.remove(mb)
                        if len(mbs_copy) == 0:
                            ans = i
                            flag = False
                        break

    print(ans)




