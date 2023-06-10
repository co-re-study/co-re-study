S, C = map(int,input().split())


chicken = []
min_chicken = 9999999
chicken_sum = 0

for _ in range(S):
    tmp = int(input())
    if min_chicken > tmp:
        min_chicken = tmp
    chicken.append(tmp)
    chicken_sum += tmp

left = 1
right = min_chicken
first_ans = 0

while left < right:
    mid = (left + right)//2

    chicken_tmp = 0
    for i0 in range(S):
        chicken_tmp += chicken[i0] // mid

    if chicken_tmp >=  C:
        left = mid+1
        first_ans = mid
    elif chicken_tmp > C:
        left = mid +1
    else:
        right = mid

print(chicken_sum - first_ans*C)



