# 좌표 압축
n = int(input())
x = list(map(int, input().split()))

x_ = sorted(list(set(x)))
# 이 상태에서 바로 index로 찾으면 매번 O(n)의 시간이 걸림
# dict로 한 번 변환하면 dict에서 O(1)의 시간으로 찾음
x_dict = {x_[i]: i for i in range(len(x_))}
for i in x:
    print(x_dict[i], end=" ")