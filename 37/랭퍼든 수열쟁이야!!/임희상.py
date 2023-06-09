n, x, y = map(int, input().split())

answer = 0
num_list = [0] * 2*n
target = y-x-1
num_list[x-1] = num_list[y-1] = target

def place_number(current):
  global answer, num_list
  
  if current == target:
    place_number(current-1)
    return
  
  if not current:
    answer += 1
    return
  
  for idx in range(2*n-current-1):
    if not num_list[idx] and not num_list[idx+current+1]:
      num_list[idx] = num_list[idx+current+1] = current
      place_number(current-1)
      num_list[idx] = num_list[idx+current+1] = 0

place_number(n)
print(answer)