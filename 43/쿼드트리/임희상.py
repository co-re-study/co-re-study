def compress(n, r1, r2, c1, c2):
  if n == 1:
    return board[r1][c1]
  
  r_mid = (r1+r2)//2
  c_mid = (c1+c2)//2
  start = board[r1][c1]
  for i in range(r1, r2):
    for j in range(c1, c2):
      if board[i][j] != start:
        return f'({compress(n//2, r1, r_mid, c1, c_mid)}{compress(n//2, r1, r_mid, c_mid, c2)}{compress(n//2, r_mid, r2, c1, c_mid)}{compress(n//2, r_mid, r2, c_mid, c2)})'
  
  return start
          

N = int(input())
board = []
for _ in range(N):
  line = list(map(int, list(input())))
  board.append(line)

print(compress(N, 0, N, 0, N))

