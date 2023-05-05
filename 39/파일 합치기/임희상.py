def split(start, end):
  if end <= start:
    return 0
  
  if memo[start][end]:
    return memo[start][end]
  
  if end == start+1:
    memo[start][end] = pages[start] + pages[end]
    return memo[start][end]
  
  min_ans = float('inf')
  
  
  for i in range(start, end):
    result = split(start, i) + split(i+1, end)
    if min_ans > result:
      min_ans = result
  memo[start][end] = min_ans + sum(pages[start:end+1])
  return memo[start][end]

T = int(input())

for _ in range(T):
  K = int(input())
  pages = list(map(int, input().split()))
  memo = [[0]*len(pages) for _ in range(len(pages))]
  
    
  print(split(0, len(pages)-1))
  