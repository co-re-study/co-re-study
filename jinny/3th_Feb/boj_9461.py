# 파도반 수열

a = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]
for tc in range(int(input())):
    n = int(input())
    if n >= len(a):
        for i in range(len(a), n + 1):
            a.append(a[i-1] + a[i-5])
    print(a[n])
# print(a)