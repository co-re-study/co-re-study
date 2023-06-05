# def P_n(i):
#     if i == 1:
#         return False
#     else:
#         for j in range(2, int(i**0.5)+1):
#             if i % j == 0:
#                 return False
#         return True


def check(num):
    num = list(str(num))
    ans = 0
    for i in num:
        ans += int(i)**2
    return ans


n = int(input())
# prime = [True for i in range(n+1)]
# for i in range(2, n+1):
#     if P_n(i) == False:
#         prime[i] = False
prime = [False, False]+[True]*(n)
plist = []
for i in range(2, n+1):
    if prime[i]:
        plist.append(i)
        for j in range(2*i, n+1, i):
            prime[j] = False
for j in range(2, n+1):
    if prime[j]:
        temp = set()
        s = j
        while True:
            num = check(s)
            if num in temp:
                if num == 1:
                    print(j)
                break
            temp.add(num)
            s = num
