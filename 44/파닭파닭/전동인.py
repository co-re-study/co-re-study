s, c = map(int, input().split())
ps = [int(input()) for _ in range(s)]

# 파의 개수와 파닭의 수가 같은 경우
if s == c:
    print(0)
else:
    start = 1
    end = max(ps)

    while start <= end:
        mid = (start + end) // 2
        count = 0

        for i in range(0, s):
            count += ps[i] // mid

        # 파의 길이가 최대가 되어야해서 휴게소 문제와는 조건이 반대
        if count >= c:
            start = mid + 1
        else:
            end = mid - 1

    # 각 파를 최대한 길게 잘랐을 때의 총 합에서 파닭에 넣은 파의 총 길이를 빼줌
    print(sum(ps) - end * c)
