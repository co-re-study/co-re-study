import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

num_set = set() # 다음에 올 숫자 목록
num_dict = dict() # key: 배수, value: 다음에 올 숫자

for num in nums[1:]:
    # 점프해서 올 수 있는 숫자라면 갱신
    if num in num_set:
        num_set.remove(num)
        for gap in num_dict:
            if num_dict[gap] == num:
                num_dict[gap] = num + gap
                num_set.add(num + gap)
        continue

    # 처음 나온 배수라면 추가
    num_set.add(num + num - nums[0])
    num_dict[num - nums[0]] = num + num - nums[0]

print(len(num_dict))

