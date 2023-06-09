def find_friend(x):
  if friends[x] == x:
    return x
  friends[x] = find_friend(friends[x])
  return friends[x]

def find_enemy(x):
  if not enemies[x]:
    return 0
  enemies[x] = find_friend(enemies[x])
  return enemies[x]
  
def union_friend(x, y):
  x = find_friend(x)
  y = find_friend(y)
  
  if (x < y):
    friends[y] = x
  else:
    friends[x] = y
    
def union_enemy(x, y):
  enemies[x] = find_friend(y)
  enemies[y] = find_friend(x)
  
  
N, M = map(int, input().split())
# 친구, 적 두 개의 배열로 적의 적은 친구다를 판단
enemies = [0] * (N+1)
friends = list(range(N+1))
answer = 1

for _ in range(M):
  one, other = map(int, input().split())
  if not answer:
    continue
  if find_friend(one) == find_friend(other):
    answer = 0
  if enemies[other]:
    union_friend(one, find_enemy(other))
  if enemies[one]:
    union_friend(other, find_enemy(one))
  union_enemy(one, other)
  
print(answer)