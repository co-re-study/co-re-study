# 차트에서 연속된 데이터의 합이 정확히 50이라면 직선이 생기므로
# 데이터의 순열로 차트를 만든다음 회전시켜보며 한쪽 그룹의 합이 50%가 되는지 확인한다.

from itertools import permutations
from collections import deque

N = int(input())
data = list(map(int, input().split()))
ans = 0

charts= list(permutations(data, N))

visited = set()
for chart in charts:
    if chart not in visited:
        chart_q = deque(chart)
        line_count = 0
        for i in range(N):
            chart_q_copy = chart_q.copy()
            left_sum = 0
            for j in range(N - i - 1): # 중복 제거
                left_sum += chart_q_copy.popleft()
                if left_sum == 50:
                    line_count += 1
                    break
                elif left_sum > 50:
                    break
            left = chart_q.popleft()
            chart_q.append(left)
        if line_count > ans:
            ans = line_count
    visited.add(chart)

print(ans)

# 2%에서 틀렸습니다 반례
# 5
# 50 10 10 10 20
# 정답
# 1