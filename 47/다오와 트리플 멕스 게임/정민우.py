# B 0 1 2 3 4
# C 0 1 2 3 4 5 
# C의 mex 6
# 아마 A에서 연속되는 값들 중 가장 큰 값 + 3하면 될듯..? 

# N = int(input())
# A = sorted(list(map(int, input().split())))
# before_a = 0
# if A[0] > 0:
#     print(0)
# else:
#     for a in A:
#         if before_a == a or before_a == a - 1:
#             before_a = a
#         else:
#             break
#     if before_a == 0:
#         print(1)
#     else:
#         print(before_a + 3)

# 40%에서 틀렸습니다, 이유는 모름

N, A = input(), sorted(list(set(map(int, input().split()))))
if A == [0]:
    print(1)
elif A[0] > 0:
    print(0)
else:
    ans = 0
    for i in range(len(A)):
        if i != A[i]:
            break
        else:
            ans = i
    print(ans + 3)
