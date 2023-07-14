def bisect(n):
    s, e = 0, len(lst)
    while s < e:
        m = (s+e)//2
        if lst[m] < n:
            s = m+1
        else:
            e = m
    return e


N = int(input())
A = list(map(int, input().split()))
lst = [0]
for num in A:
    if lst[-1] < num:
        lst.append(num)
    else:
        lst[bisect(num)] = num
print(len(lst)-1)

# N = int(input())
# A = list(map(int, input().split()))
# lst = [0]
# for num in A:
#     if lst[-1] < num:
#         lst.append(num)
#     else:
#         s, e = 0, len(lst)
#         while s < e:
#             m = (s+e)//2
#             if lst[m] < num:
#                 s = m+1
#             else:
#                 e = m
#         lst[e] = num
# print(len(lst)-1)
