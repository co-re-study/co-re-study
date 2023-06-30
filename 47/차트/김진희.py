# 차트
def same_teritory(circle):
    global answer
    ans = -1
    start = 0
    end = 0
    while end < len(circle):
        sum_sub = 0
        for i in range(end - start + 1):
            sum_sub += circle[start + i]
        if sum_sub == 50:
            ans += 1
            start += 1
            end += 1
        elif sum_sub > 50:
            start += 1
        else:
            end += 1
    if answer < ans:
        answer = ans
    return


def perm(depth):
    if depth == n:
        same_teritory(sel)
        return

    for i in range(n):
        if not check[i]:
            check[i] = 1
            sel[depth] = dogs[i]
            perm(depth+1)
            check[i] = 0


n = int(input())
dogs = list(map(int, input().split()))
answer = 0
# 50 있으면 무조건 한 줄
if 50 in dogs:
    print(1)
# 50 이상 있으면 0줄
elif max(dogs) > 50:
    print(0)
else:
    sel = [0]*n 
    check = [0]*n
    perm(0)
    print(answer)
