from itertools import combinations
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    mbti_lst = list(map(str, input().split()))

    mbti_dict = Counter(mbti_lst)

    max_cnt = max(mbti_dict.values())

    if max_cnt >= 3:
        print(0)

    else:  # max_cnt = 1, 2

        combs = combinations(mbti_lst, 3)

        min_d = 12
        for comb in combs:
            a, b, c = comb

            d = 0
            for i in range(4):
                if a[i] == b[i] == c[i]:
                    pass
                else:
                    d += 2

            if d < min_d:
                min_d = d

        print(min_d)


# ---

# 비트마스킹으로 풀기


# 문자열을 이진 표현으로 매핑
mbti_to_binary = {'E': 0, 'I': 1, 'N': 0,
                  'S': 1, 'F': 0, 'T': 1, 'P': 0, 'J': 1}

t = int(input())

for _ in range(t):
    n = int(input())
    mbti_lst = list(map(str, input().split()))

    # MBTI 유형을 이진 표현으로 변환
    binary_lst = [sum(mbti_to_binary[ch] << (3 - i)
                      for i, ch in enumerate(mbti)) for mbti in mbti_lst]

    min_dist = 12
    for a, b, c in combinations(binary_lst, 3):

        # XOR 연산을 사용하여 두 유형 간의 차이를 계산
        dist = bin(a ^ b).count('1') + \
            bin(b ^ c).count('1') + bin(a ^ c).count('1')

        # dist = 0
        # for el in [a ^ b, b ^ c, c ^ a]:
        #     for i in range(4):
        #         if el & (1 << i):
        #             dist += 1

        min_dist = min(min_dist, dist)

    print(min_dist)
