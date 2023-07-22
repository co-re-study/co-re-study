T = int(input())
for _ in range(T):
    N = int(input())
    mbti = list(input().split())
    ans = 12
    if N > 32:
        print(0)
    else:
        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    temp = 0
                    for l in range(4):
                        if mbti[i][l] != mbti[j][l]:
                            temp += 1
                        if mbti[i][l] != mbti[k][l]:
                            temp += 1
                        if mbti[j][l] != mbti[k][l]:
                            temp += 1
                    ans = min(temp, ans)
        print(ans)
