# import sys
# input= sys.stdin.readline
#
# N = int(input())
# for i in range(N):
#     s = list(input().rstrip())
#     reversed_s = list(reversed(s))
#     flag = True
#     # 회문 탐색
#     for j in range(len(s)):
#         if reversed_s[j] != s[j]:
#             flag = False
#             break
#     if flag:
#         print("0")
#         continue
#
#     # 유사회문 탐색
#     else:
#         answer = 2
#         for j in range(len(s)):
#             candi_s = s[:j] + s[j+1:]
#             reversed_candi_s = list(reversed(candi_s))
#             flag = True
#             for k in range(len(candi_s)):
#                 if reversed_candi_s[k] != candi_s[k]:
#                     flag = False
#                     break
#             if flag:
#                 answer = 1
#                 break
#         print(answer)

# 2차 시도
# 3중 for문 제거 위해 투 포인터 적용
import sys
input= sys.stdin.readline
N = int(input())
for i in range(N):
    s = list(input().rstrip())
    reversed_s = list(reversed(s))
    flag = True
    # 회문 탐색
    for j in range(len(s)):
        if reversed_s[j] != s[j]:
            flag = False
            break
    if flag:
        print("0")
        continue
    # 유사 회문 탐색
    else:
        answer = 2
        left = 0
        right = len(s)-1
        check = False
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                candi_s = s[:right] + s[right+1:]
                if candi_s == candi_s[::-1]:
                    check = True
                    break
                candi_s = s[:left] + s[left+1:]
                if candi_s == candi_s[::-1]:
                    check = True
                    break
                else:
                    break
        if check:
            print("1")
        else:
            print("2")


