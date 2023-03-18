# 네네무
n = int(input())  # 수
first_root = int(n ** (1/2) // 1)  # 제일 큰 제곱근
ans = [0, 0, 0, 0, 0]
while first_root:
    parent = n - (first_root ** 2)
    answer = [first_root]
    while parent:
        if len(answer) >= len(ans):
            break
        next_root = int(parent ** (1/2) // 1)
        parent -= (next_root ** 2)
        answer.append(next_root)
    if len(answer) < len(ans):
        ans = answer
    first_root -= 1
print(len(ans))