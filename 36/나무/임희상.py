N, M = map(int, input().split())

trees = list(map(int, input().split()))

left = 0
right = 2000000000
target = 0
while left <= right:
  current = (left + right) // 2
  
  timber = 0
  for tree in trees:
    if tree > current:
      timber += tree - current
  if target == current:
    break
  target = current
  if timber < M:
    right = current
  elif timber > M:
    left = current
print(target)