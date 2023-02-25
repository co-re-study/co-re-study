# 잃어버린 괄호
problem = input()
num = []
operate = [0]
start = 0
for i in range(len(problem)):
    if problem[i] == '+' or problem[i] == '-':
        num.append(int(problem[start:i]))
        operate.append(problem[i])
        start = i + 1
else:
    num.append(int(problem[start:]))
answer = num[0]
minus = 0
ans = 0
for n in range(1, len(num)):
    if operate[n] == '-':
        if minus:
            answer -= ans
        else:
            answer += ans
        ans = num[n]
        minus = 1
    elif operate[n] == '+':
        if minus:
            ans += num[n]
        else:
            answer += num[n]
    # print('minus', minus)
    # print('answer', answer)
    # print('ans', ans)
if ans:
    answer -= ans
print(answer)