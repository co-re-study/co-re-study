import sys
T = int(input())

for _ in range(T):
  P, M, F, C = map(int, sys.stdin.readline().split())
  # input으로 받으면 시간초과
  
  init_coupons = C * (M // P)
  chicken_1 = init_coupons // F
  chicken_2 = 0
  current = min(init_coupons, F)
  if init_coupons > F:
    chicken_2 += (init_coupons-F) // (F-C)
    current += (init_coupons-F) % (F-C)
  
  while current >= F:
    chicken = current // F
    chicken_2 += chicken
    current -= chicken * F
    current += chicken * C
    
  print(chicken_2 - chicken_1)