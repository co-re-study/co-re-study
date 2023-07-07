n = int(input())
nums = list(map(int, input().split()))

tail = [0] * n  # 최장 증가 부분 수열을 저장할 배열
tail[0] = nums[0]
length = 1

for i in range(1, n):
    if nums[i] < tail[0]:  # nums[i]가 현재까지의 최장 증가 부분 수열의 최솟값보다 작을 경우
        tail[0] = nums[i]
    elif nums[i] > tail[length-1]:  # nums[i]가 현재까지의 최장 증가 부분 수열의 최댓값보다 클 경우
        tail[length] = nums[i]
        length += 1
    else:  # nums[i]가 현재까지의 최장 증가 부분 수열의 어느 위치에 들어갈지 이분 탐색으로 찾음
        s, e = 0, length - 1
        while s < e:
            m = (s + e) // 2
            if tail[m] < nums[i]:  # 타겟보다 작은 수 중에서 가장 큰 수를 찾는다.
                s = m + 1  # 타겟보다 작아야하니까 s를 움직임
            else:
                e = m
        tail[s] = nums[i]

print(length)
