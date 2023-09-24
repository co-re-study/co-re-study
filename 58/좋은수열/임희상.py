def determine(idx):

    for i in range(1, idx//2+1):
        if nums[-i:] == nums[-2*i:-i]:
            return False
        
    if idx == N:
        return ''.join(nums)

    for i in range(1, 4):
        nums.append(str(i))
        answer = determine(idx+1)
        if answer:
            return answer
        nums.pop()

N = int(input())
nums = []
print(determine(0))