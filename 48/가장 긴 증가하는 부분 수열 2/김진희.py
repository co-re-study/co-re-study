# 가장 긴 증가하는 부분 수열 2
def binary_search(x):
    start = 0
    end = len(sub_nums) - 1
    while start < end:
        if end - start == 1:
            if x < sub_nums[end]:
                sub_nums[end] = x
            elif x < sub_nums[start]:
                sub_nums[start] = x
            return
        middle = (start + end) // 2
        if sub_nums[middle] > x:
            end = middle
        elif sub_nums[middle] < x:
            start = middle
        else:
            return


n = int(input())
nums = [0] + list(map(int, input().split()))
sub_nums = [0, nums[1]]
for i in range(2, n + 1):
    # 가장 큰 수는 맨 뒤에 추가
    if nums[i] > sub_nums[-1]:
        sub_nums.append(nums[i])
    # 이분 탐색으로 위치 찾기
    else:
        binary_search(nums[i])

print(len(sub_nums) - 1)
