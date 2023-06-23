w, h, k = map(int, input().split())
# 주의! 아래 녀석은 높이다.
n = int(input())
cut_ver = [0] + list(map(int, input().split())) + [h]
# 주의! 아래 녀석은 너비다.
m = int(input())
cut_hor = [0] + list(map(int, input().split())) + [w]

# 조각난 높이와 너비를 오름차순으로 정렬
diff_hor = sorted([cut_hor[i+1] - cut_hor[i] for i in range(m+1)])
diff_ver = sorted([cut_ver[j+1] - cut_ver[j] for j in range(n+1)])

# 너비의 시작과 높이의 끝에 포인터를 두고 이동시키면서 개수를 세아린다.
cnt = 0
i, j = 0, n
while i < m+1 and j >= 0:
    if diff_hor[i] * diff_ver[j] <= k:
        cnt += j + 1
        i += 1
    else:
        j -= 1

print(cnt)
