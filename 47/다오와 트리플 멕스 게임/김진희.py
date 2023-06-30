# 다오와 트리플 멕스 게임
def blank():
    start = 0
    end = n - 1
    while start < end:
        middle = (start + end) // 2
        if a[middle] == middle:
            start = middle
            if end - start == 1:
                return start + 3
        else:
            if a[middle - 1] == middle - 1:
                return middle + 2
            else:
                end = middle


N = int(input())
a = list(set(map(int, input().split())))
n = len(a)
if n == 1:
    print(0) if a[0] else print(1)
else:
    a.sort()
    # 배열에 0이 없으면 0
    if a[0]:
        print(0)
    # 배열에 0이 있을 때
    else:
        if a[-1] == n - 1:
            print(a[-1] + 3)
        else:
            print(blank())
