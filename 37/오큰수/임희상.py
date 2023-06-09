from collections import deque
N = int(input())

sequence = list(map(int, input().split()))
rising_seq = deque([])
answers = []

for i in range(N-1, -1, -1):
  num = sequence[i]
  if not rising_seq or num >= rising_seq[-1]:
    rising_seq = deque([num])
    answers.append(-1)
  else:
    while True:
      current = rising_seq.popleft()
      if current > num:
        answers.append(current)
        rising_seq.appendleft(current)
        rising_seq.appendleft(num)
        break
        
print(*answers[::-1])
