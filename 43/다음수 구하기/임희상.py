T = int(input())

for t in range(T):
  nums = list(input())
  target = [nums[-1]]
  for i in range(len(nums) - 2, -1, -1):
    if nums[i] < nums[i+1]:
      target.sort()
      for j in range(len(target)):
        if target[j] > nums[i]:
          nums[i], target[j] = target[j], nums[i]
          break
      ans = ''.join(nums[:i+1] + sorted(target))
      break
    else:
      target.append(nums[i])
  else:
    ans = 'BIGGEST'
    
  print(ans)
    
