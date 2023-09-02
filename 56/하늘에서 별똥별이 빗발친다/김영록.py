import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())
ans = 0
stars = [list(map(int, input().split())) for _ in range(K)]
for i in range(K):
    for j in range(K):
        temp = 0
        for k in range(K):
            if stars[i][0] <= stars[k][0] <= stars[i][0]+L and stars[j][1] <= stars[k][1] <= stars[j][1]+L:
                temp += 1
        ans = max(ans, temp)
print(K-ans)
