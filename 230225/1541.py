fomula = input().split('-')
nums = []
for i in fomula:
    if '+' in i:
        nums.append(sum(map(int, i.split('+'))))
    else:
        nums.append(int(i))

result = nums[0]
for num in nums[1:]:
    result -= num

print(result)