N, A, lis = int(input()), list(map(int, input().split())), []

for a in A:
    if not lis or lis[-1] < a:
        lis.append(a)
    elif a < lis[0]:
        lis[0] = a
    else:
        l, c, r = 0, len(lis) // 2, len(lis)
        while True:
            if lis[c] == a:
                break
            elif lis[c] < a and l == c:
                lis[c + 1] = a
                break
            elif a < lis[c]:
                r, c = c, (c + l) // 2
            elif lis[c] < a:
                l, c = c, (c + r) // 2
print(len(lis))