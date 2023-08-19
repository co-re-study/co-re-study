N = int(input())
num_list = list(map(int, input().split()))

start, end = 0, 0
answer = 0
memo = [0 for _ in range(100001)]
while start < N and end < N:
    if not memo[num_list[end]]:
        memo[num_list[end]] = 1
        end += 1
        answer += (end - start)
    else:
        memo[num_list[start]] = 0
        start += 1
print(answer)