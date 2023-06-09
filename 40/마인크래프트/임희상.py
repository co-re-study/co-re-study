N, M, B = map(int, input().split())
board = []
heights = [0] * 257
max_height = 0
min_height = 257
for _ in range(N):
  line = list(map(int, input().split()))
  line_max = max(line)
  line_min = min(line)
  if line_max > max_height:
    max_height = line_max
  if line_min < min_height:
    min_height = line_min
  for j in range(M):
    heights[line[j]] += 1
  board.append(line)

min_ans = 256*N*M
target_height = 0

for target in range(max_height, min_height-1, -1):
  current = 0
  blocks = B
  for height in range(max_height, min_height-1, -1):
    if target > height:
      current += (target - height) * heights[height]
      blocks -= (target - height) * heights[height]
      if blocks < 0:
        break
    else:
      current += (height - target) * 2 * heights[height]
      blocks += (height - target) * heights[height]
      
  else:
    if current < min_ans:
      min_ans = current
      target_height = target

print(min_ans, target_height)