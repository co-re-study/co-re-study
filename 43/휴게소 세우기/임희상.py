N, M, L = map(int, input().split())

stations = set(map(int, input().split()))

for k in range(1, L):
  
  current = 0
  left = M
  for i in range(1, L):
    current += 1
    if i in stations:
      current = 0
    if current >= k:
      if not left:
        break
      left -= 1
      current = 0
    
  else:
    print(k)
    break
  