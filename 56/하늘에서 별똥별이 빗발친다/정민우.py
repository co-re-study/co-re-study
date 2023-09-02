# 모든 좌표 다 돌면서 사각형 그리면 시간초과

# 별똥별이 떨어질 자리 두개를 골라서 각 x, y 최소값을 좌상단 꼭지점으로 하는 L길이의 사각형 만들기

# 그냥 조합으로 했더니 오답, 별똥별 하나를 꼭지점으로 할 수도 있도록 중복조합으로 풀었더니 정답

from itertools import combinations_with_replacement

N, M, L, K = map(int, input().split())
stars = [tuple(map(int, input().split())) for _ in range(K)]
ans = 0

for s1, s2 in combinations_with_replacement(stars, 2):
    left, top = min(s1[0], s2[0]), min(s1[1], s2[1])
    right, bottom = left + L, top + L
    count = 0
    for x, y in stars:
        if left <= x <= right and top <= y <= bottom:
            count += 1
    if ans < count:
        ans = count

print(len(stars) - ans)