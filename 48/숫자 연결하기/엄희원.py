N, M = map(int, input().split())

str_N = str(N)

re_set = set()

flag = True

num = 0

cnt = 1

while flag:
    if N % M == 0:
        print(cnt)
        break

    else:
        if N % M not in re_set:
            re_set.add(N % M)
            N = int(str(N % M) + str_N)
            cnt += 1
        else:
            print(-1)
            break

