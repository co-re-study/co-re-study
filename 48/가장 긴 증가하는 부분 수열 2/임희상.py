
N = int(input())
nums = list(map(int, input().split()))
lis = []
lis.append(nums[0])


for num in nums:

    if num > lis[-1]:
        lis.append(num)

    elif num < lis[0]:
        lis[0] = num

    else:
        left = 0
        right = len(lis)

        while left < right:
            mid = (left + right) // 2
            if lis[mid] < num:
                left = mid + 1
            else:
                right = mid

        lis[right] = num

print(len(lis))
