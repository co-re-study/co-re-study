import sys, heapq
input = sys.stdin.readline

N, M, L = map(int, input().split())

# N > 0
if N:
    nums = sorted(list(map(int, input().split())))

    # 최대 gap과 gap 리스트 구하기
    max_gap = max(nums[0], L - nums[-1])
    gaps = [nums[0], L - nums[-1]]
    for i in range(len(nums)-1):
        gap = nums[i + 1] - nums[i]
        gaps.append(gap)
        if gap > max_gap:
            max_gap = gap
    gaps.sort()

    left = 1
    right = max_gap

    # 이분탐색
    while left <= right:
        middle = (left + right) // 2
        flag = False
        
        # 최댓값 뽑기 위해 힙에 음수로 저장
        negative_gaps = list(map(lambda x: -x, gaps))
        heapq.heapify(negative_gaps)
        cnt = 0
        while negative_gaps:
            current = -heapq.heappop(negative_gaps)
            # 최대 gap이 현재 추정값보다 크면 추정값으로 잘라서 다시 힙에 넣기
            if current > middle:
                heapq.heappush(negative_gaps, -middle)
                heapq.heappush(negative_gaps, -(current - middle))
                cnt += 1
                # M보다 휴게소를 많이 세웠으면 추정값 더 키우기
                if cnt > M:
                    left = middle + 1
                    break
            else:
                flag = True
                break
        
        # 휴게소를 다 세우기 전에 추정값이 모든 gap보다 커진 경우
        if flag:
            # 현재 정답보다 추정값이 더 작은 경우 갱신
            if middle < max_gap:
                max_gap = middle
            # 둘이 같은 경우 break
            elif middle == max_gap:
                break
            # 추정값 더 줄이기
            right = middle - 1

    print(max_gap)

# N == 0
else:
    answer = L // (M + 1)
    answer += 1 if L % (M + 1) else 0
    print(answer)
